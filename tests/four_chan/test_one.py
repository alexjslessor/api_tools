from ..conftest import *


@pytest.mark.asyncio
class Test_Dependancies:

    async def test_get_chan(self):
        data = get_catalog(Board.b)
        assert data is not None
        assert len(data) > 0
        pprint(data)
        # print(jsonable_encoder(data))



# insert json array into mongodb
# async def insert_json_array(collection, json_array):
#     await collection.insert_many(json_array)
#     return True































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

