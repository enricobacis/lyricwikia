from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()

setup(name='lyricwikia',
      version='0.1.0',
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
