from httpx import AsyncClient
import pytest
import asyncio
# import httpx
from typing import Dict, Any, List
from asgi_lifespan import LifespanManager
from pydantic import *
from pprint import pprint
# from starlette.status import (
#     HTTP_404_NOT_FOUND, 
#     HTTP_422_UNPROCESSABLE_ENTITY, 
#     HTTP_200_OK,
#     HTTP_400_BAD_REQUEST
# )
# from bson import Decimal128
from osint_tools.db import *
from osint_tools.api import *
from osint_tools.settings import get_settings

settings = get_settings()

mon_db = MongoCrud(settings.MONGO_URI, settings.MONGO_DB_NAME)
db = mon_db.get_mongo_db()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

# @pytest.fixture
# async def test_client():
#     async with LifespanManager(app):
#         async with httpx.AsyncClient(
#             app=app, 
#             base_url="http://app.io") as test_client:
#             yield test_client


