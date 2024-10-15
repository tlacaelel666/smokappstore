import os.path
import re
import uuid
from os import abort
from urllib import response
from urllib.parse import urlparse, parse_qs

import yt_dlp
from flask import Flask, send_file

app = Flask(__name__)
file_uuid = str(uuid.uuid4)

youtube_regex = re.compile(
    f'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
)
def valid_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme in ["http", "https"]:
        return ValueError

def sanitize_url(url):
    if youtube_regex.match(url):
        parsed_url = urlparse(url)
        if 'youtube' in parsed_url.netloc:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get('v')
            if video_id:
              return f"https://www.youtube.com/watch?v=(video_id[0])"
        if 'yutu.be' in parsed_url.netloc:
            video_id = parsed_url.path.lstrip('/')
            return f"https://www.youtube.com/watch?v={video_id}"

        return None

def convert_url(request_url, method='get'):
    if method.get_form: request_url = yt_dlp.get_urls
    request_url.YoutubeDL.download(),
    return audio_file(response)

def audio_file(response):
     if __name__ == '__main__':
        return response(send_file('mp3'))
