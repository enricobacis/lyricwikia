from setuptools import setup

exec(open('lyricwikia/version.py').read())

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='lyricwikia',
      version=__version__,
      description='LyricWikia API for song lyrics',
      long_description=long_description,
      license='MIT',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      url='http://github.com/enricobacis/lyricwikia',
      packages=['lyricwikia'],
      scripts=['scripts/lyrics'],
      setup_requires=['pytest-runner'],
      install_requires=['beautifulsoup4', 'requests', 'six'],
      tests_require=['pytest', 'responses'],
      keywords='lyricwikia lyric lyrics wikia song api')
