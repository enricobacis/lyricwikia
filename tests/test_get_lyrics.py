from lyricwikia import get_lyrics, LyricsNotFound
import responses
import pytest


@responses.activate
def test_returnLyrics():

    responses.add(responses.GET,
                  'https://lyrics.wikia.com/wiki/Lyricwikia:Lyricwikia',
                  body=('<div class="lyricbox">thank<br/>you.</div>'))

    lyrics = get_lyrics("Lyricwikia", "Lyricwikia")
    print repr(lyrics)
    assert len(responses.calls) == 1
    assert lyrics == "thank\nyou."


@responses.activate
def test_returnLyricsNotFound():
    responses.add(responses.GET,
                  'https://lyrics.wikia.com/wiki/Lyricwikia:Lyricwikia',
                  body='')

    with pytest.raises(LyricsNotFound):
        get_lyrics('Lyricwikia', 'Lyricwikia')
    assert len(responses.calls) == 1
