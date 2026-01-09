import json
FILE="youtube.txt"
def load_data():
    try:
        with open(FILE,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(FILE,"w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print(f"{index}:{video}",end="\n")

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter time limit : ")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)
    
    
def update_video_details():
    pass

def delete_video(video):
    pass

def main():
    videos=load_data()

    while True:
        print("\nYoutube Manager | Make a choice : \n1.List all videos\n2.Add Video in favorite\n3.Update video details\n4.Delete Video\n5.Exit\n")
        choice=input("Enter your choice : ")

        match choice :
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
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
