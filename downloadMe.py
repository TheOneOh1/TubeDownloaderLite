from pytube import YouTube
from sys import argv


link = input("Enter Video Link : " )
vid = YouTube(link)

print("\n============================================================================\n")

print("Title : ", vid.title)

down = vid.streams.get_by_itag(22)
down.download()

#You can save the downloaded video in a specific path down.download('path')

print("\nVideo Download Complete")

print("\n============================================================================\n")
