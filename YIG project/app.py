from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
import re
from urllib.parse import urlparse, parse_qs
from datetime import datetime
from zoneinfo import ZoneInfo
import os
from dotenv import load_dotenv


# API_KEY = "AIzaSyDSUF3XyYpa8eeiTpLq1FJnZnz3gCGhAdc"
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)


app = Flask(__name__, template_folder="templates")

def get_id_from_url(url):
    if "watch?v=" in url:
        video_id = parse_qs(urlparse(url).query)["v"][0]
    elif "youtu.be/" in url:
        video_id = url.split("/")[-1]
    elif "/shorts/" in url:
        video_id = url.split("/shorts/")[1].split("?")[0]
    else:
        return ""
    return video_id


# def get_thumbnail_url(video_id):
#     request = youtube.videos().list(
#         part="snippet,statistics,contentDetails",
#         id=video_id
#     )
#     response = request.execute()
#     video = response['item'][0]

#     thumbnail = video["snippet"]["thumbnails"]["high"]["url"]
#     return thumbnail



@app.route('/get-summary', methods=['POST'])
def get_info():
    data = request.get_json()
    user_url = data.get('url', '')

    video_id = get_id_from_url(user_url)
    requestt = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=video_id
        )
    response = requestt.execute()
    video = response['items'][0]
    title = video["snippet"]["title"]
    description = video["snippet"]["description"]
    channel = video["snippet"]["channelTitle"]

    views = video["statistics"]["viewCount"]
    likes = video["statistics"]["likeCount"]
    comments = video["statistics"]["commentCount"]

    duration = video["contentDetails"]["duration"]
    published_at = video["snippet"]["publishedAt"]
    utc_time = datetime.strptime(
    published_at,
        "%Y-%m-%dT%H:%M:%SZ"
    ).replace(tzinfo=ZoneInfo("UTC"))

    user_timezone = data.get("timezone", "UTC")

    local_time = utc_time.astimezone(ZoneInfo(user_timezone))

    formatted = local_time.strftime("%d.%m.%Y %H:%M")

    thumbnail_url = video["snippet"]["thumbnails"]["high"]["url"]

    def format_duration(duration):
        h = re.search(r"(\d+)H", duration)
        m = re.search(r"(\d+)M", duration)
        s = re.search(r"(\d+)S", duration)

        hours = int(h.group(1)) if h else 0
        minutes = int(m.group(1)) if m else 0
        seconds = int(s.group(1)) if s else 0

        if hours:
            return f"{hours}:{minutes:02}:{seconds:02}"
        return f"{minutes}:{seconds:02}"

    # Bu yerda backend'ingiz to'liq matnni tayyorlaydi
    generated_text = (
        f"YouTube Video Information\n"
        f"{'=' * 50}\n\n"

        f"Title       : {title}\n"
        f"Channel     : {channel}\n"

        f"Views       : {views}\n"
        f"Likes       : {likes}\n"
        f"Comments    : {comments}\n"
        f"Duration    : {format_duration(duration)}\n"
        f"Published   : {formatted}  {user_timezone}\n\n\n"

        #f"Description :\n{description}\n\n"
    )

    return jsonify({'result': generated_text,
                    'thumbnail': thumbnail_url
                    })



@app.route('/')
def base():
    return render_template('index.html')




if __name__ =='__main__':
    app.run(debug=True)