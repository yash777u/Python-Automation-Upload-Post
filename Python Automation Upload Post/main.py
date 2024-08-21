import time
import random
from instagrapi import Client
import os

def login(username, password):
    try:
        cl = Client()
        cl.login(username, password)
        print("Logged in successfully!")
        return cl
    except Exception as e:
        print("Failed to login:", e)
        return None

def upload_images(client):
    images_folder = "./images"
    if not os.path.exists(images_folder):
        print("Images folder not found.")
        return
    
    image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
    for image_file in image_files:
        try:
            image_path = os.path.join(images_folder, image_file)
            client.photo_upload(image_path, caption="Tags 🏷: #animeaesthetic #animeedit #animevibes #oldanime #animesadquotes #explore #love #sadquote #lovequote #explorepage #quote #animelover #animeforlife #quotesandsaying #naruto #gardenofwords #lifequotes #lifegoals #motivationalquotes #lovequotes #quotesaboutlife #lovelifequotes #lifesayings #animelife #animelovequotes #animesliceoflife #animelove #animemotivation #animeindia #anime ")
            print(f"Uploaded image: {image_file}")
        except Exception as e:
            print(f"Failed to upload image '{image_file}':", e)

def clip_upload(client):
    videos_folder = "./videos"
    if not os.path.exists(videos_folder):
        print("Videos folder not found.")
        return
    
    video_files = [f for f in os.listdir(videos_folder) if os.path.isfile(os.path.join(videos_folder, f))]
    for video_file in video_files:
        try:
            video_path = os.path.join(videos_folder, video_file)
            client.video_upload(video_path, caption=" Tags 🏷: #animeaesthetic #animeedit #animevibes #oldanime #animesadquotes #explore #love #sadquote #lovequote #explorepage #quote #animelover #animeforlife #quotesandsaying #naruto #gardenofwords #lifequotes #lifegoals #motivationalquotes #lovequotes #quotesaboutlife #lovelifequotes #lifesayings #animelife #animelovequotes #animesliceoflife #animelove #animemotivation #animeindia #anime ")
            print(f"Uploaded video: {video_file}")
            
            # Add a random delay between 30 and 40 seconds
            delay = random.randint(30, 40)
            print(f"Waiting for {delay} seconds before uploading the next video...")
            time.sleep(delay)
            
        except Exception as e:
            print(f"Failed to upload video '{video_file}':", e)

def main():
    # Replace these with your Instagram credentials
    username = "username"
    password = "pass"
    
    # Log in
    client = login(username, password)
    if client is None:
        return
    
    while True:
        print("Select an option:")
        print("1. Upload images from /images folder")
        print("2. Upload videos from /videos folder")
        print("3. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            upload_images(client)
        elif choice == "2":
            clip_upload(client)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
