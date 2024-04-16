import requests
import time

def get_rtsp_video_stats():
    start_time = time.time()
    response = requests.get('http://localhost:5000/rtsp_stream')
    video_bitrate = len(response.content) * 8 / (time.time() - start_time)  # Calculate bitrate
    video_execution_time = time.time() - start_time
    return video_bitrate, video_execution_time

def get_mpeg_dash_video_stats():
    start_time = time.time()
    response = requests.get('http://localhost:5000/mpeg_dash_stream')
    video_bitrate = len(response.content) * 8 / (time.time() - start_time)  # Calculate bitrate
    video_execution_time = time.time() - start_time
    return video_bitrate, video_execution_time


if __name__ == '__main__':
    rtsp_bitrate, rtsp_execution_time = get_rtsp_video_stats()
    print("RTSP Video Bitrate:", rtsp_bitrate)
    print("RTSP Video Execution Time:", rtsp_execution_time)
    
    mpeg_dash_bitrate, mpeg_dash_execution_time = get_mpeg_dash_video_stats()
    print("MPEG-DASH Video Bitrate:", mpeg_dash_bitrate)
    print("MPEG-DASH Video Execution Time:", mpeg_dash_execution_time)