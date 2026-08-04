from flask import Flask, render_template, request
from googleapiclient.discovery import build
import re
from pytube import YouTube


API_KEY = "AIzaSyDSUF3XyYpa8eeiTpLq1FJnZnz3gCGhAdc"

youtube = build("youtube", "v3", developerKey=API_KEY)


app = Flask(__name__, template_folder="templates")


def get_thumbnail_url(youtube_url: str) -> str:
    match = re.search(r"(?:v=|\/([0-9A-Za-z_-]{11}).*|list=|\/shorts\/)([0-9A-Za-z_-]{11})", youtube_url)
    if match:
        video_id = match.group(1) or match.group(2)
        return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return ""

def get_thumbnail_from_url(video_url):
    url = str(video_url)
    yt = YouTube(url)
    print("Sarlavha:", yt.title)
    print("Kanal:", yt.author)
    print("Ko'rishlar:", yt.views)
    print("Davomiyligi (soniya):", yt.length)
    print("Thumbnail URL:", yt.thumbnail_url)  # Thumbnail rasmi havolasi


@app.route('/')
def base():
    return render_template('index.html')




if __name__ =='__main__':
    app.run(debug=True)