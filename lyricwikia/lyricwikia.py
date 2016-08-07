from bs4 import BeautifulSoup
import requests

__BASE_URL__ = 'http://lyrics.wikia.com/wiki'

def create_url(artist, song):
    """Create the URL in the LyricWikia format"""
    return '{base_url}/{artist}:{song}'.format(
            base_url=__BASE_URL__,
            artist='_'.join(artist.title().split()),
            song='_'.join(song.title().split()))

def get_lyrics(artist, song, linesep='\n'):
    """Retrieve the lyrics of the song"""
    url = create_url(artist, song)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    lyricbox = soup.find('div', {'class': 'lyricbox'})

    if not lyricbox:
        raise Exception('Cannot download lyrics')
    for br in lyricbox.findAll('br'):
        br.replace_with(linesep)
    return lyricbox.text.strip()
