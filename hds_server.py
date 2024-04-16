from conf import MP4_FILE_PATH, PROTOCOL_CONF
from flask import Flask, Response

app = Flask(__name__)

@app.route(PROTOCOL_CONF['HDS']['endpoint'])
def video():
    def generate():
        video_path = MP4_FILE_PATH
        chunk_size = 1024

        with open(video_path, 'rb') as video_file:
            while True:
                video_chunk = video_file.read(chunk_size)
                if not video_chunk:
                    break

                yield video_chunk

    return Response(generate(), mimetype='application/octet-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)