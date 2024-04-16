from conf import get_url

import json
import subprocess


HDS_URL = "http://localhost:8000/hds_stream"
DOWNLOAD_CMD = ['wget', HDS_URL]
MEDIAINFO_CMD = [ 'mediainfo', '--Output=JSON', HDS_URL]


if __name__ == '__main__':
    # subprocess.run(DOWNLOAD_CMD)

    mediainfo_output = subprocess.check_output(MEDIAINFO_CMD)
    json_output = json.loads(mediainfo_output)
    
    bitrate = json_output['media']['track'][1]['BitRate']
    duration = json_output['media']['track'][1]['Duration']

    print(f"Bitrate: {bitrate}")
    print(f"Duration: {duration}")