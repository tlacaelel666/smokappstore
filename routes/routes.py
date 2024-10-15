from flask import Blueprint, render_template, request
from werkzeug.utils import send_file

from utils.converter import convert_mp3

main = Blueprint('main', __name__)


@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/converter', method=['GET','POST'])
def converter():
    url = request.form.get('url')
    if url:
        audio_file = convert_mp3()
        return send_file(audio_file, as_attachment=True, environ=type[str])
    return "Error: invalid URL"
