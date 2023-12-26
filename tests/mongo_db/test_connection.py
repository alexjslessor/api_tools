from ..conftest import *
from pprint import pprint

@pytest.mark.asyncio
class Test_MongoDB:
    async def test_get_db_name(self):
        c = mon_db.get_db_name
        pprint(c)

    async def test_conn(self):
        c = await mon_db.get_build_info
        pprint(c)

    async def test_get_coll_names(self):
        c = await mon_db.get_collection_names
        pprint(c)