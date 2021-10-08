from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from ordered_set import OrderedSet


class Crawler():

    def __init__(self, url, depth=25):
        self.crawled_urls = OrderedSet([])

    def crawl(self, url):
        return
