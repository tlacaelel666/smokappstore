import os

from flask import jsonify, Flask
from pytube import YouTube
from yt_dlp import YoutubeDL

from routes.routes import converter

app = Flask(__name__)


#principal path to convert url to mp3
def convert_mp3():
    url = converter.form.get['url']
    if not url:
        return jsonify({'error': 'no url provided'}), 400

    ydl_opts = {
        'format': 'best audio/best',
        'output': 'mp3_file',
        'postprocessors': [{
            'ffmpeg': "ExtractAudio",
            'preferred codec': 'mp3',
            'preferred quality': '192'
        }],
        "outtmpl": 'file_name/%(title)s.%(ext)s'
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
             yt = YouTube(url)
             video = yt.streams.filter(only_audio=True)
             request = video(download=True)
             info_dict = ydl.extract_info(request)
             audio_file = os.path.join('tmp', f"{info_dict['title']}.mp3")
        output_path = f"{os.getcwd()}/output.mp3"
        return jsonify({'success': True, output_path: audio_file}), 200

    except Exception as e:
     return jsonify({'error': str(e)}), 500
