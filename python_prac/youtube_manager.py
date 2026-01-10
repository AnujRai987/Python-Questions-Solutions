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
    print("\n")
    print("*"*75)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. Name: {video['Name']} , Duration: {video['Duration']}")
    print("\n")
    print("*"*75)

def add_video(videos):
    name=input("Enter video name: ")
    duration=input("Enter time limit : ")
    videos.append({"Name":name,"Duration":duration})
    save_data_helper(videos)
    
    
def update_video_details(videos):
    index=int(input("Enter video number to update :"))
    if(1<=index<=len(videos)):
        name=input("Enter video name : ")
        duration=input("Enter time limit : ")
        videos[index-1]={'Name':name,'Duration':duration}
        save_data_helper(videos)
    else:
        print("Invalid input")


def delete_video(videos):
    index=int(input("Enter video number to delete: "))
    del videos[index-1]
    save_data_helper(videos)

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
                update_video_details(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice !!\n")



if __name__ =="__main__":
    main()
