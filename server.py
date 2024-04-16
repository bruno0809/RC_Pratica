from flask import Flask, Response
import subprocess

MP4_VIDEO_PATH = r'/home/bfaiao/Videos/teste2.mp4'

app = Flask(__name__)

@app.route('/rtsp_stream')
def rtsp_stream():
    return Response(stream_video('rtsp'), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/mpeg_dash_stream')
def mpeg_dash_stream():
    return Response(stream_video('mpeg-dash'), mimetype='application/dash+xml')


def stream_video(protocol):
    if protocol == 'rtsp':
        cmd = ['ffmpeg', '-i', MP4_VIDEO_PATH, '-c:v', 'libx264', '-preset', 'veryfast', '-profile:v', 'baseline', '-f', 'rtsp', 'rtsp://localhost:8554/live']
    elif protocol == 'mpeg-dash':
        cmd = ['ffmpeg', '-re', '-i', MP4_VIDEO_PATH, '-c:v', 'libx264', '-preset', 'veryfast', '-profile:v', 'baseline', '-f', 'dash', '-']
    ffmpeg_process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    while True:
        frame = ffmpeg_process.stdout.read(1024)
        if not frame:
            break
        yield (frame)

if __name__ == '__main__' :
    app.run()