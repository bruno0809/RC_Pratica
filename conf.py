SERVER_URL = 'http://localhost'

MP4_FILE_PATH = './teste2.mp4'

PROTOCOL_CONF = {
    'HDS': {
        'endpoint': '/hds_stream',
        'port': ':8000',

    },
    'MPEG-DASH': {
        'endpoint': '/mpeg-dash_stream',
        'port': ':5000',

    },    
}


def get_url(protocol):
    ''' Getter for stream URL '''
    return SERVER_URL + PROTOCOL_CONF[protocol]['port'] + PROTOCOL_CONF[protocol]['endpoint']