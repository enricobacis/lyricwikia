__all__ = ['__version__', 'get_lyrics', 'Song', 'Artist', 'LyricsNotFound']

from .lyricwikia import get_lyrics, Song, Artist
from .lyricwikia import LyricsNotFound
from .version import __version__
