from conf import PROTOCOL_CONF, MP4_FILE_PATH
from flask import Flask, Response

import subprocess


FFMPEG_CMD = ['ffmpeg', '-re', '-i', MP4_FILE_PATH, '-c:v', 'libx264', '-preset', 'veryfast', '-profile:v', 'baseline', '-f', 'dash', '-']

app = Flask(__name__)

@app.route(PROTOCOL_CONF['MPEG-DASH']['endpoint'])
def mpeg_dash_stream():
    return Response(stream_video(), mimetype='application/dash+xml')

def stream_video():
    ffmpeg_process = subprocess.Popen(FFMPEG_CMD, stdout=subprocess.PIPE)
    while True:
        frame = ffmpeg_process.stdout.read(1024)
        if not frame:
            break
        yield (frame)

if __name__ == '__main__' :
    app.run()