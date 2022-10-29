from ..conftest import *

rss = RSSFeed()
feed_test = 'http://feedparser.org/docs/examples/rss20.xml'

# @pytest.mark.asyncio
class Test_RSS:
    def test_get_rss(self):
        all_feeds = []
        for url in EnumRSS.list_name_or_value('value'):
            print(url)
            all_feeds += rss.get_feed(url)
        pprint(all_feeds)

