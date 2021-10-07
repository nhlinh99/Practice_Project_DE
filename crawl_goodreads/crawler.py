from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from ordered_set import OrderedSet
from .helper import is_url_valid, get_clean_url, is_link_internal


class Crawler():

    def __init__(self, url, depth=25):
        self.crawled_urls = OrderedSet([])
        if (is_url_valid(url)):
            url = get_clean_url(url, '')
            self.depth = depth
            self.index = 0
            self.crawl(url)

    def crawl(self, url):
        return
