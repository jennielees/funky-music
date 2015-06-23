import urllib
import requests

SEARCH_URL = 'https://api.spotify.com/v1/search'


def get_music(mood, limit=10, offset=0):
    """ Gets playlist recommendations from the Spotify
        API for music with a specific mood, by the simple
        expedient of searching playlists for that term. (:
    """
    data = {
        'q': mood,
        'type': 'playlist',
        'limit': limit,
        'offset': offset
    }

    url = "{}?{}".format(SEARCH_URL, urllib.urlencode(data))

    print url  # - Uncomment this and see what it's doing

    r = requests.get(url).json()

    assert 'playlists' in r

    return r['playlists']['items']
