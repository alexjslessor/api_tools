from httpx import AsyncClient
import pytest
import asyncio
from typing import Any
from asgi_lifespan import LifespanManager
from pydantic import *
from pprint import pprint

from osint_tools.rss import RSS_Schema, RSSFeed, EnumRSS
from osint_tools.four_chan import *
# from osint_tools.gpt_promptify import *
# from osint_tools.translator.schema.schema import (
    # TranslatorLangCodes, 
    # TessLangCodes
# )
# from osint_tools.ocr_pdf import *

from osint_tools.db import *
from osint_tools.settings import get_settings
# from osint_tools.entry_dev import app
# from osint_tools.utils.utils import *

settings = get_settings()
mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
db = mon_db.get_mongo_db()
# file_list = get_lang_test_files()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

# @pytest.fixture
# async def test_client():
#     base_url="http://localhost"
#     async with LifespanManager(app):
#         async with AsyncClient(
#             app=app, 
#             base_url=base_url
#             ) as test_client:
#             yield test_client



# def test_file_helper():
    # l = get_lang_test_files()
    # print(l)


# red_conn = get_redis_connection(encoding='utf-8', decode_responses=True)
# @pytest.fixture
# def r_conn() -> get_redis_connection:
    # return red_conn