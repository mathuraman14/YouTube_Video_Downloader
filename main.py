import shutil
import yt_dlp
import os
from googleapiclient.discovery import build

# Replace with your YouTube Data API key
API_KEY = 'YOUR_API_KEY'

# Replace with your playlist ID
playlist_link = input('Enter YouTube Playlist Link: ')
split_here = '='
res = playlist_link.split(split_here, 1)
PLAYLIST_ID = res[1]
print("PLAYLIST ID = ",PLAYLIST_ID)

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_playlist_name(playlist_id):
    request = youtube.playlists().list(
        part='snippet',
        id=playlist_id
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]['snippet']['title']
    else:
        #raise ValueError('Playlist not found or no items found.')
        folder_name: str = r"D:\Videos\YouTubeVideoDownloader"
        os.makedirs(folder_name, exist_ok=True)

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_link])

def create_folder_and_download(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f'Folder "{folder_name}" created.')
    else:
        print(f'Folder "{folder_name}" already exists.')
    # Download the playlist using yt-dlp
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_link])

    # Zip the directory containing the downloaded videos
    shutil.make_archive(folder_name, 'zip', folder_name)
    print(folder_name + " zipped successfully.")
def main():
    try:
        playlist_name = get_playlist_name(PLAYLIST_ID)
        playlist_name_folder = r"D:\Videos\\" + playlist_name
        print("Final Folder : ", playlist_name_folder)
        create_folder_and_download(playlist_name_folder)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
