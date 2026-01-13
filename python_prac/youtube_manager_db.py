import sqlite3

conn=sqlite3.connect("youtube.db")
cur=conn.cursor()

def list_all_videos():
    pass
def add_video():
    cur.execute("CREATE TABLE IF NOT EXIST videos()")

def update_video():
    pass
def delete_video():
    pass


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

if __name__ == "__name__":
    main()
