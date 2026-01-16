import requests

url="https://api.freeapi.app/api/v1/public/randomproducts/product/random"
response = requests.get(url)
data =response.json()

print(data["data"]["id"])
