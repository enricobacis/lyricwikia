lyricwikia
==========

Python API to get song lyrics from `LyricWikia`_

.. image:: https://travis-ci.org/enricobacis/lyricwikia.svg?branch=master
    :target: https://travis-ci.org/enricobacis/lyricwikia


Description
-----------

`LyricWikia`_ is an online wiki-based lyrics database and encyclopedia.
It used to provide full access to song lyrics via API, but the service
has been discontinued.

This API scrapes the song web page and returns the lyrics. Please verify
that your use complies with the `LyricWikia`_ terms of service.


Installation
------------

The package ``lyricwikia`` is on `PyPI`_, so you can install it using pip:

.. code::

    pip install lyricwikia

Otherwise download this repository and use the ``setup.py`` file:

.. code::

    python setup.py install


Usage
-----

You can use the ``lyrics`` command to look for a song lyrics.

    usage: lyrics [-h] [--separator SEPARATOR] [--version] ARTIST SONG

    Get lyrics of a song from LyricWikia

    positional arguments:
      ARTIST                Artist name
      SONG                  Song title

    optional arguments:
      -h, --help            show this help message and exit
      --separator SEPARATOR
                            line separator
      --version             show program's version number and exit


Example
-------

.. code::

    $ lyrics 'Led Zeppelin' 'Stairway to heaven'
    There's a lady who's sure all that glitters is gold
    ...


API
---

At the moment ``lyricwikia`` provides two APIs that are not officially already
provided by the official APIs):

- ``get_lyrics(artist, song, linesep='\n', timeout=None)``: returns a string
    that contains the lyrics of the song as provided by LyricWikia. If the
    lyrics is not found, the ``LyricsNotFound`` exception is raised.
  
- ``get_all_lyrics(artist, song, linesep='\n', timeout=None)``: returns a list
  of all the lyrics versions of the song (e.g., both the *kanji* and the
  *romaji* versions if available).  If the lyrics is not found, the
  ``LyricsNotFound`` exception is raised.


.. code:: python

    import lyricwikia
    lyrics = lyricwikia.get_lyrics('Led Zeppelin', 'Stairway to heaven')


Used by
-------

- `spotify-downloader`_: download Spotify playlists with albumart and meta-tags


.. _LyricWikia: http://lyrics.wikia.com
.. _PyPI: https://pypi.python.org/pypi/lyricwikia
.. _spotify-downloader: https://github.com/ritiek/spotify-downloader
