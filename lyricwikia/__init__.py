from .lyricwikia import get_lyrics, get_all_lyrics
from .lyricwikia import Song, Artist, LyricsNotFound
from .version import __version__

__all__ = ['get_lyrics', 'get_all_lyrics',
           'Song', 'Artist', 'LyricsNotFound', '__version__']
