import os
import shutil
import yt_dlp

#Define the playlist URL and directory
playlist_url = input('Enter YouTube Playlist Link: ')
download_dir = r'D:\Videos\{Your_Playlist_Link}'

#Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

#Download the playlist using yt-dlp
ydl_opts = {
    'format': 'best',
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

#Zip the directory containing the downloaded videos
shutil.make_archive(download_dir, 'zip', download_dir)