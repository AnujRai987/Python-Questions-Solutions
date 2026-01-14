import sqlite3

conn=sqlite3.connect("youtube.db")
cur=conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                duration TEXT NOT NULL
    )''')

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

    conn.commit()

def add_video():
    name=input("Enter video name :")
    duration=input("Enter the vidoe duration :")
    cur.execute("INSERT INTO videos(name,duration) VALUES(?,?)",(name,duration))
    conn.commit()

def update_video():
    id=input("Enter video ID want to update :")
    name=input("Enter the name to be updated :")
    duration=input("Enter new duration :")
    
    cur.execute("UPDATE videos SET name=?,duration=?  WHERE id=?",(name,duration,id))
    conn.commit()
    
def delete_video():
    id=input("Enter Video ID want to delete : ")
    cur.execute("DELETE FROM videos WHERE id =?",(id))
    conn.commit()

def main():
    while True:
        print("\nYoutube Manager | Make a choice : \n1.List all videos\n2.Add Video in favorite\n3.Update video details\n4.Delete Video\n5.Exit\n")
        choice=input("Enter your choice : ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid choice !!")



    conn.close()        

if __name__ == "__main__":
    main()
