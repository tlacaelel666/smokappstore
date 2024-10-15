import os

from flask import send_from_directory, abort
from pydub import AudioSegment
from pytube import YouTube

from run import app



def download():
    return send_from_directory("tmp/filename", as_attachment=True, path="UPLOAD_FOLDER")

DOWNLOAD_FOLDER = os.path.join, (os.path.dirname(app.instance_path), 'downloads')
app.config['UPLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024
if os.path.exists(f"convert"):

    if not os.path.exists('DOWNLOAD_FOLDER'):
        os.mkdir('DOWNLOAD_FOLDER')
def download_file(file_id):
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'tmp')
    app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024
    if os.path.exists(f"convert"):
        file_name = f"{file_id}.mp3"
        audio_file = os.path.join('DOWNLOAD_FOLDER')
        if not os.path.exists('DOWNLOAD_FOLDER'):
            os.mkdir('DOWNLOAD_FOLDER')
    if os.path.exists('DOWNLOAD_FOLDER'):
     return audio_file.post(self=file_name)
    else:
        return 404, abort(404)
if __name__=='__main__':
    app.run(debug=True)


def convert():
    yt = YouTube("url required")
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = f"{yt.title}.mp3"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file)
    audio_stream.convert_url()
    audio = AudioSegment.from_file(output_path)
    audio.export(output_path, format='mp3')
    return send_from_directory(app.config['UPLOAD_FOLDER'], audio_file, as_attachment=True)



