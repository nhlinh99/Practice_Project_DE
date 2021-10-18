from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


class Crawler():

    def __init__(self, url, depth=25):
        self.crawled_urls = []

    def crawl(self, url):
        return
