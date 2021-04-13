# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import atoma
import feedparser
import requests


def get_python_insider_news():
    response = requests.get('http://feeds.feedburner.com/PythonInsider?fmt=xml')
    feed = atoma.parse_atom_bytes(response.content)
    t = 0
    d = feedparser.parse(url_file_stream_or_string='view-source:http://feeds.feedburner.com/PythonInsider?fmt=xml')
    entries = d['entries']
    t = 0

def get_pep_news():
    d = feedparser.parse(url_file_stream_or_string='https://www.python.org/dev/peps/peps.rss')
    entries = d['entries']
    t = 0


def get_django_news():
    d = feedparser.parse(url_file_stream_or_string='https://www.djangoproject.com/rss/weblog/')
    entries = d['entries']
    t = 0

def get_pycharm_news():
    d = feedparser.parse(url_file_stream_or_string='https://blog.jetbrains.com/pycharm/feed/')
    entries = d['entries']
    t = 0

def get_psf_news():
    response = requests.get('http://pyfound.blogspot.com/atom.xml')
    feed = atoma.parse_atom_bytes(response.content)
    t = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_python_insider_news()
    get_pep_news()
    get_django_news()
    get_pycharm_news()
    get_psf_news()
