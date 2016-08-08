from setuptools import setup

exec(open('lyricwikia/version.py').read())

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='lyricwikia',
      version=__version__,
      description='LyricWikia API for song lyrics',
      long_description=long_description,
      install_requires=[
          'beautifulsoup4',
          'requests',
      ],
      url='http://github.com/enricobacis/lyricwikia',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['lyricwikia'],
      scripts=['scripts/lyrics'],
      keywords='lyricwikia lyric lyrics wikia song api'
)
