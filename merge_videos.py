import sys
import os
import subprocess

from pytube import YouTube

def download_yt_video(url):
    name = YouTube(url).streams.first().download()
    newname = name.replace(' ','_')
    os.rename(name,newname)
    return newname

if __name__ == "__main__":
    # Download youtube videos
    links = ["https://www.youtube.com/watch?v=hh7Gu3MsGH8"] * 2  # Quickest dab ever
    filenames = [ download_yt_video(link) for link in links ]

    print(filenames)

    # Process with ffmpeg
    command = "ffmpeg -i {} -i {} -filter_complex hstack output.mp4".format(filenames[0], filenames[1])

    subprocess.call(command, shell=True)

    
