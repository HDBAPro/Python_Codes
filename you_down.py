#
#   PyThon Learning  @Faymaz
#       @programirez
#
# pip install yt-dlp
import yt-dlp

# Enter the url for the download
url = input("Enter video url: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")
