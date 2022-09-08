from osint_tools.api.email.gmail.deps import EmailAcct
from ..conftest import *


@pytest.mark.asyncio
class Test_Dependancies:

    async def test_email(self):
        e = EmailAcct(
            account_email=settings.TEST_EMAIL,
            app_password=settings.GMAIL_APP_PASSWORD
        )
        # print(e.list_inboxes)
        # emails = e.conn.search(None, 'ALL')
        # emails = e.search_emails('a')
        # emails = e.get_recent()
        emails = e.list_mail()
        print(emails)


























# class Decorators:

#     def timefunc(func):
#         def f(*args, **kwargs):
#             from time import time
#             start = time()
#             rv = func(*args, **kwargs)
#             finish = time()
#             print('Run time is.', finish - start)
#             return rv
#         return f


# @pytest.mark.asyncio
# class Test_Dependancies:

#     # @Decorators.timefunc
#     # async def test_get_chan_v2(self):
#         # data = await get_catalog_v2()
#         # pprint(data)

#     @Decorators.timefunc
#     async def test_get_chan(self):
#         data = get_catalog()
#         # pprint(data)

#     # async def test_chan_schema(self):
#     #     data = get_catalog()[0]
#     #     assert isinstance(data, BaseModel)

