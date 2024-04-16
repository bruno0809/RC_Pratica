from conf import get_url

import requests
import time


def get_mpeg_dash_video_stats():
    start_time = time.time()
    response = requests.get(get_url('MPEG-DASH'))
    video_bitrate = len(response.content) * 8 / (time.time() - start_time) 
    video_execution_time = time.time() - start_time
    return video_bitrate, video_execution_time


if __name__ == '__main__':
    mpeg_dash_bitrate, mpeg_dash_execution_time = get_mpeg_dash_video_stats()
    print("MPEG-DASH Video Bitrate:", mpeg_dash_bitrate)
    print("MPEG-DASH Video Execution Time:", mpeg_dash_execution_time)