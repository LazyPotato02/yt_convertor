from pytube import YouTube
import os

print("\n Youtube To MP3\n")

url = input("Enter Video URL:")
yt = YouTube(url)

try:
    print("\nDownloading...")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\n Successfilly Downloaded\n")

except:
    print("Something weng wrong! Try again...")