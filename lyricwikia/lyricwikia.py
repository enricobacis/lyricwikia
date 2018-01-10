from six.moves.urllib.parse import quote as _quote
from bs4 import BeautifulSoup as _BeautifulSoup
import requests as _requests

__BASE_URL__ = 'https://lyrics.wikia.com'


class LyricsNotFound(Exception):
    __module__ = Exception.__module__

    def __init__(self, message=None):
        super(LyricsNotFound, self).__init__(message)


def urlize(string):
    """Convert string to LyricWikia format"""
    return _quote('_'.join(string.title().split()))


def create_url(artist, song):
    """Create the URL in the LyricWikia format"""
    return (__BASE_URL__ +
            '/wiki/{artist}:{song}'.format(artist=urlize(artist),
                                           song=urlize(song)))


def get_lyrics(artist, song, linesep='\n', timeout=None):
    """Retrieve the lyrics of the song"""
    url = create_url(artist, song)
    response = _requests.get(url, timeout=timeout)
    soup = _BeautifulSoup(response.content, "html.parser")
    lyricbox = soup.find('div', {'class': 'lyricbox'})

    if not lyricbox:
        raise LyricsNotFound('Cannot download lyrics')
    for br in lyricbox.findAll('br'):
        br.replace_with(linesep)
    return lyricbox.text.strip()


class Song(object):
    """A Song backed by the LyricWikia API"""

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    @property
    def lyrics(self):
        """Song lyrics obtained by parsing the LyricWikia page"""
        return get_lyrics(self.artist, self.title)

    def __str__(self):
        return "Song(artist='%s', title='%s')" % (self.artist, self.title)

    def __repr__(self):
        return str(self)


class Album(object):
    """An Album backed by the LyricWikia API"""

    def __init__(self, artist, album_data):
        self.artist = artist
        self.title = album_data['album']
        self.year = album_data['year']
        self.songs = [Song(artist, song) for song in album_data['songs']]

    def __str__(self):
        return "Album(artist='%s', title='%s')" % (self.artist, self.title)

    def __repr__(self):
        return str(self)


class Artist(object):
    """An Artist backed by the LyricWikia API"""

    __API__ = __BASE_URL__ + '/api.php?fmt=json&func=getArtist&artist={artist}'

    def __init__(self, name):
        url = self.__API__.format(artist=urlize(name))
        data = _requests.get(url).json()
        self.name = data['artist']
        self.albums = [Album(self.name, album) for album in data['albums']]

    def __str__(self):
        return "Artist(name='%s')" % (self.name)

    def __repr__(self):
        return str(self)
