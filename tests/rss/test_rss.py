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
        class _URLModel(BaseModel):
            url: HttpUrl

        def _parse_url(url: str):
            try:
                url_model = _URLModel(url=url)
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

        _parse_url(url1)

    def test_get_urls(self):
        urls = EnumRSS.list_name_or_value('value')
        data = RssSchemaList.from_url_list(urls, limit=2)
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

    @pytest.mark.asyncio
    async def test_to_db_v2(self):
        urls = EnumRSS.list_name_or_value('value')
        data = RssSchemaList.to_db_v2(
            db=db,
            urls=urls,
            collection='rss',
            filter_field='article_id',
            limit=2
        )
        print('len: ', len(data.rss_list))
        assert data.rss_list, 'no rss list'
        # is_deleted = await db['rss'].delete_many({})
        # print(f'is_Deleted: {is_deleted.deleted_count}')
        is_updated = await data.bulk_create_or_update(db, 'rss')
        print(f'is_updated: {is_updated}')
