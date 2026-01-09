import json
FILE="youtube.txt"
def load_data():
    try:
        with open(FILE,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File is not Found.")

def save_data_helper(video):
    with open(FILE,"w") as file:
        json.dumps(video)

def list_all_videos():
    print(load_data())

def add_video():
    name=input("Enter video name: ")
    time=input("Enter time limit : ")
    video=f"{"{name}:{time}"}"
    save_data_helper(video)
    
def update_video_details(video):
    pass
def delete_video():
    pass


def main():
    videos=load_data()

    while True:
        print("\nYoutube Manager | Make a choice : \n1.List all videos\n2.Add Video in favorite\n3.Update video details\n4.Delete Video\n5.Exit\n")
        choice=input("Enter your choice : ")

        match choice :
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Invalid choice !!\n")



if __name__ =="__main__":
    main()