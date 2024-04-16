SERVER_URL = 'http://localhost:5000'

MP4_FILE_PATH = './teste2.mp4'

PROTOCOL_CONF = {
    'HDS': {
        'endpoint': '/hds_stream',

    },
    'MPEG-DASH': {
        'endpoint': '/mpeg-dash_stream',

    },    
}


def get_url(protocol):
    ''' Getter for stream URL '''
    return SERVER_URL + PROTOCOL_CONF[protocol]['endpoint']