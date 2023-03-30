from pytube import YouTube
from moviepy.editor import *
import os

def convertmp4file(filename):
    def MP4ToMP3(mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()

    VIDEO_FILE_PATH = (f"{filename}.mp4")
    AUDIO_FILE_PATH = (f"{filename}.mp3")

    MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

def audiodownload(yt):
    stream = yt.streams.get_by_itag(140)
    stream.download()
    print("Audio Downloaded!")

    convertmp4file(filename=title)
    print("Audio Converted!")
    os.remove(f"{title}.mp4")

def videodownload(yt):
    stream = yt.streams.get_by_itag(399)
    stream.download()
    print("Video Downloaded!")

def main():
    link = input("Enter link to video? \n")
    yt = YouTube(link)

    print(f"Title: {yt.title} \n")
    print(f"Description: {yt.description} \n")
    print(f"Views: {yt.views} \n")
    print(f"Channel ID: {yt.channel_id} \n")
    
    global title
    title = yt.title

    choice = str(input("Do you want to download the video? (y/n): \n")).lower().strip()
    choice1 = str(input("Do you want to download the video or audio? (audio/video): \n")).lower().strip()
    if choice == "y":
        if choice1 == "audio":
            audiodownload(yt)
        elif choice1 == "video":
            videodownload(yt)
    else:
        print("Bye!")

main()