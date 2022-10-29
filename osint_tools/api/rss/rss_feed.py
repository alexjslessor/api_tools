import feedparser
from ..base import *

class RSSFeed(object):
    def get_feed(self, url: str):
        d = feedparser.parse(url)
        rss = []
        for k in d['entries']:
            post = {}
            for k, v in k.items():
                post[k] = v
            rss.append(RSS_Schema(**post).dict())
        return rss
