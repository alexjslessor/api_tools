from ..conftest import *

from redis_om import get_redis_connection
from redis_om import HashModel

redis_conn = get_redis_connection()


@pytest.mark.asyncio
class Test_REDIS_CHAN:

    async def test_one(self):
        data = get_catalog(Board.pol.value)
        # print(data)
        for catalog_model in data:
            # print(catalog_model)

            # r = redis_conn.set(catalog_model.no, catalog_model.json())
            # r = redis_conn.msetnx(catalog_model.dict())
            # r = redis_conn.lset(catalog_model.dict())
            r = redis_conn.hset(
                'pol', 
                catalog_model.no, 
                catalog_model.json()
                )

            print(r)

    # async def test_delete_data(self):
        # redis_conn.flushdb()


'''
data = {
    'dog': {
        'scientific-name' : 'Canis familiaris'
    }
}
r = redis.Redis()
r.json().set('doc', '$', data)
doc = r.json().get('doc', '$')
dog = r.json().get('doc', '$.dog')
scientific_name = r.json().get('doc', '$..scientific-name')
'''






