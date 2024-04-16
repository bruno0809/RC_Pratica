from conf import get_url

import json
import subprocess


DOWNLOAD_CMD = ['wget', '-O', 'streamed.mp4', get_url('HDS')]
MEDIAINFO_CMD = [ 'mediainfo', '--Output=JSON', 'streamed.mp4']


if __name__ == '__main__':
    subprocess.run(DOWNLOAD_CMD)
    mediainfo_output = subprocess.check_output(MEDIAINFO_CMD)
    json_output = json.loads(mediainfo_output)
    
    bitrate = json_output['media']['track'][1]['BitRate']
    duration = json_output['media']['track'][1]['Duration']

    print(f"Bitrate: {bitrate}")
    print(f"Duration: {duration}")