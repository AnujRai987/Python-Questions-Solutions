"""
live_binance_predict_fixed.py

- Fetch historical klines from Binance REST API
- Feature engineering
- Walk-forward (TimeSeriesSplit) CV to estimate realistic performance
- Train final XGBoost classifier
- Connect to Binance websocket for live 1m kline updates
- On each closed candle, compute features on rolling window and show prediction

Fixes:
- Replaces deprecated pandas .append() with pd.concat()
- Removes deprecated XGBoost param
- Adds walk-forward CV reporting
"""

import json
import time
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score
import xgboost as xgb
import ta
from websocket import WebSocketApp
import joblib
import warnings
warnings.filterwarnings("ignore")

# ----------------- CONFIG -----------------
SYMBOL = "BTCUSDT"       # change as needed
INTERVAL = "1m"          # Binance interval
H = 1                    # horizon in intervals (predict close at t+H)
WINDOW = 200             # rolling window size for live features
TRAIN_HISTORY = 2000     # number of historical candles to fetch for training
THRESHOLD = 0.55         # probability threshold to label UP
# ------------------------------------------

def fetch_klines(symbol, interval, limit=1000):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    cols = ["open_time","open","high","low","close","volume","close_time","qav","num_trades","taker_base","taker_quote","ignore"]
    df = pd.DataFrame(data, columns=cols)
    df["datetime"] = pd.to_datetime(df["open_time"], unit="ms")
    df = df[["datetime","open","high","low","close","volume"]].astype(
        {"open":"float","high":"float","low":"float","close":"float","volume":"float"})
    return df

def make_features(df):
    df = df.copy()
    df = df.sort_values("datetime").reset_index(drop=True)
    # returns & lags
    df["ret_1"] = df["close"].pct_change(1)
    for l in [1,2,3,5,10]:
        df[f"ret_lag_{l}"] = df["close"].pct_change(l)
    # candle features
    df["body"] = df["close"] - df["open"]
    df["upper_wick"] = df["high"] - df[["close","open"]].max(axis=1)
    df["lower_wick"] = df[["open","close"]].min(axis=1) - df["low"]
    df["range"] = df["high"] - df["low"]
    # indicators
    df["ema_5"] = ta.trend.ema_indicator(df["close"], window=5)
    df["ema_13"] = ta.trend.ema_indicator(df["close"], window=13)
    df["sma_20"] = ta.trend.sma_indicator(df["close"], window=20)
    df["rsi_14"] = ta.momentum.rsi(df["close"], window=14)
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["atr_14"] = ta.volatility.average_true_range(df["high"], df["low"], df["close"], window=14)
    # volatility
    df["vola_10"] = df["ret_1"].rolling(10).std()
    df["vola_30"] = df["ret_1"].rolling(30).std()
    # cyclical time of day
    df["minute"] = df["datetime"].dt.hour * 60 + df["datetime"].dt.minute
    df["minute_sin"] = np.sin(2 * np.pi * df["minute"] / 1440)
    df["minute_cos"] = np.cos(2 * np.pi * df["minute"] / 1440)
    return df

def add_labels(df, horizon):
    df = df.copy()
    df["future_close"] = df["close"].shift(-horizon)
    df["target"] = (df["future_close"] > df["close"]).astype(int)
    return df

def select_feature_columns():
    cols = [
        "ret_lag_1","ret_lag_2","ret_lag_3","ret_lag_5","ret_lag_10",
        "body","upper_wick","lower_wick","range",
        "ema_5","ema_13","sma_20","rsi_14","macd","macd_signal","atr_14",
        "vola_10","vola_30","minute_sin","minute_cos"
    ]
    return cols

def prepare_training_data(df, horizon):
    df_feat = make_features(df)
    df_feat = add_labels(df_feat, horizon)
    df_feat = df_feat.dropna().reset_index(drop=True)
    feature_cols = select_feature_columns()
    X = df_feat[feature_cols].copy()
    y = df_feat["target"].copy()
    return df_feat, X, y

def train_xgb(X, y):
    model = xgb.XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        eval_metric="logloss",
        n_jobs=4,
        random_state=42
    )
    model.fit(X, y)
    return model

def timeseries_cv_report(X, y, n_splits=5):
    tscv = TimeSeriesSplit(n_splits=n_splits)
    results = []
    fold = 0
    for train_idx, test_idx in tscv.split(X):
        fold += 1
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        m = xgb.XGBClassifier(n_estimators=200, max_depth=4, learning_rate=0.05,
                              eval_metric="logloss", n_jobs=4, random_state=42)
        m.fit(X_train, y_train)
        pprob = m.predict_proba(X_test)[:,1]
        preds = (pprob > 0.5).astype(int)
        acc = accuracy_score(y_test, preds)
        auc = roc_auc_score(y_test, pprob)
        prec = precision_score(y_test, preds, zero_division=0)
        rec = recall_score(y_test, preds, zero_division=0)
        results.append({"fold":fold, "acc":acc, "auc":auc, "prec":prec, "rec":rec, "trades":len(y_test)})
        print(f"Fold {fold}: acc={acc:.4f}, auc={auc:.4f}, prec={prec:.4f}, rec={rec:.4f}, test_size={len(y_test)}")
    dfres = pd.DataFrame(results)
    print("\nCV mean:\n", dfres.drop(columns="fold").mean().to_dict())
    return dfres

# ----------------- MAIN -----------------
print("Downloading historical candles...")
hist = fetch_klines(SYMBOL, INTERVAL, limit=TRAIN_HISTORY)
print(f"Downloaded {len(hist)} candles for {SYMBOL} {INTERVAL}")

# Prepare training data
df_feat, X, y = prepare_training_data(hist, H)
print("Training data shape:", X.shape)
print("Positive class ratio (UP):", y.mean())

# Timeseries CV report (walk-forward)
print("\nRunning TimeSeriesSplit CV (walk-forward) to estimate performance...")
cv_res = timeseries_cv_report(X, y, n_splits=5)

# Train final model on all data
print("\nTraining final XGBoost on full dataset...")
model = train_xgb(X, y)
print("Model trained.")

# Save model
joblib.dump(model, "xgb_binance_model.joblib")
print("Saved model to xgb_binance_model.joblib")

# Check in-sample metrics (for reference only)
pp = model.predict_proba(X)[:,1]
preds_in = (pp > 0.5).astype(int)
print(f"In-sample accuracy: {accuracy_score(y, preds_in):.4f}, AUC: {roc_auc_score(y, pp):.4f}")

# ----------------- LIVE WEBSOCKET SETUP -----------------
# Start rolling_df with most recent candles (for live predictions)
rolling_df = hist.copy().tail(WINDOW).reset_index(drop=True)

def candle_to_df_row(candle_ms, o, h, l, c, v):
    """Return one-row DataFrame for a closed candle.
       candle_ms is milliseconds since epoch (int)."""
    row = pd.DataFrame([{
        "datetime": pd.to_datetime(candle_ms, unit='ms'),
        "open": float(o),
        "high": float(h),
        "low": float(l),
        "close": float(c),
        "volume": float(v)
    }])
    return row

def on_message(ws, message):
    global rolling_df, model
    try:
        msg = json.loads(message)
    except Exception as e:
        print("Failed to parse message:", e)
        return

    if "k" not in msg:
        return
    k = msg["k"]
    is_closed = k.get("x", False)
    if not is_closed:
        # ignore unfinished candle for consistency
        return

    # build new candle row
    t_ms = k["t"]
    new_row = candle_to_df_row(t_ms, k["o"], k["h"], k["l"], k["c"], k["v"])

    # concatenate instead of append
    rolling_df = pd.concat([rolling_df, new_row], ignore_index=True)
    # keep last WINDOW
    if len(rolling_df) > WINDOW:
        rolling_df = rolling_df.iloc[-WINDOW:].reset_index(drop=True)

    # compute features and predict
    df_f = make_features(rolling_df).dropna().reset_index(drop=True)
    if df_f.empty:
        print("Not enough data yet to compute indicators (waiting for more closed candles).")
        return

    latest = df_f.iloc[-1:].copy()
    feature_cols = select_feature_columns()
    X_live = latest[feature_cols].values
    if np.isnan(X_live).any():
        print("NaNs in live features; skipping prediction for this candle.")
        return

    prob_up = model.predict_proba(X_live)[0,1]
    decision = "UP" if prob_up > THRESHOLD else "DOWN"
    timestamp = latest["datetime"].iloc[0]
    price = float(latest["close"].iloc[0])
    print(f"[{pd.to_datetime(timestamp)}] price={price:.2f}  prob_up={prob_up:.3f}  -> {decision}")

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed:", close_status_code, close_msg)

def on_open(ws):
    print("WebSocket connection opened.")

# Start websocket
stream_name = f"{SYMBOL.lower()}@kline_{INTERVAL}"
ws_url = f"wss://stream.binance.com:9443/ws/{stream_name}"
print("Connecting to websocket:", ws_url)

ws = WebSocketApp(ws_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)

try:
    ws.run_forever()
except KeyboardInterrupt:
    print("Interrupted by user — closing.")
except Exception as e:
    print("Websocket run_forever exception:", e)
