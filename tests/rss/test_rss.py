from ..conftest import *
from osint_tools.rss import *
from pydantic import BaseModel, HttpUrl
from urllib.parse import urlparse

feed_test = 'http://feedparser.org/docs/examples/rss20.xml'
id1 = 'https://www.haaretz.com/srv/haaretz-latest-headlines'
id2 = 'https://www.haaretz.com/israel-news/2023-12-20/ty-article/.premium/arab-israeli-doctor-leaves-job-after-being-wrongly-accused-of-supporting-terrorism/0000018c-8730-dc3e-addd-d7b018c50000'
url1 = "https://www.example.com/path?query=123#fragment"

class TestRss:
    def test_url_1(self):
        r = urlparse(url1)
        print(f'url1: {r.path}')

    def test_create_uids(self):
        class URLModel(BaseModel):
            url: HttpUrl

        def parse_url(url: str):
            try:
                url_model = URLModel(url=url)
                parsed_url = urlparse(url_model.url)
                idx = {
                    "scheme": parsed_url.scheme,
                    "netloc": parsed_url.netloc,
                    "path": parsed_url.path,
                    "params": parsed_url.params,
                    "query": parsed_url.query,
                    "fragment": parsed_url.fragment
                }
                print(idx)
            except Exception as e:
                raise
        parse_url(url1)

    def test_get_urls(self):
        urls = EnumRSS.list_name_or_value('value')
        data = RssSchemaList.get_urls(urls)
        assert data.rss_list, 'no rss list'
        return data

    @pytest.mark.asyncio
    async def test_to_db(self):
        data = self.test_get_urls()
        assert data.rss_list, 'no rss list'
        await data.to_db(
            db,
            'rss',
            'article_id', 
        )
