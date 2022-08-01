from cmath import exp
from pytube import YouTube
from sys import argv


link = input("Enter Video Link : " )
try:
    vid = YouTube(link)

    print("\n============================================================================\n")

    print("Title : ", vid.title)

    down = vid.streams.get_by_itag(22)
    print("downloading video....")
    down.download()

    #You can save the downloaded video in a specific path down.download('path')

    print("\nVideo Download Complete")

    print("\n============================================================================\n")
except Exception as e:
    print("Something went wrong with the link, more information is provided below.")
    print(e)
