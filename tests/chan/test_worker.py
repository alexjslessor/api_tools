from tests.conftest import *
from pymongo import ReplaceOne

TEST_COLLECTION: str = '4chan_test_collection'

@pytest.mark.asyncio
class TestWorker:

    async def test_replace_chan(self):
        data = get_catalog(Board.pol)
        update = []
        for catalog_model in data:
            update.append(
                ReplaceOne(
                    {'no': catalog_model.no}, 
                    catalog_model.dict(), 
                    upsert=True)
            )
        assert len(update) >= 10, f'check update list len: {update}'
        logger.info(update[:1])
        return update


    async def test_insert_chan(self,):
        update = await self.test_replace_chan()

        idx = await mon_db.create_unique_idx(db[TEST_COLLECTION], 'no')
        assert idx is not None, f'create_unique_idx is None: {idx}'

        result = await db[TEST_COLLECTION].bulk_write(update)
        assert result is not None, f'result is none'

        assert result.bulk_api_result['writeErrors'] == [], 'has errors'
        assert result.bulk_api_result['writeConcernErrors'] == [], 'has write concerns'

        logger.info(f'nModified: {result.bulk_api_result['nModified']!s}')
        logger.info(f'nUpserted: {result.bulk_api_result['nUpserted']!s}')
        logger.info(f'nInserted: {result.bulk_api_result['nInserted']!s}')
        logger.info(f'nRemoved: {result.bulk_api_result['nRemoved']!s}')
        logger.info(f'nMatched: {result.bulk_api_result['nMatched']!s}')
        logger.info(f'upserted: {result.bulk_api_result['upserted']!s}')


@pytest.mark.asyncio
class Test_Chan_DB:
    @pytest.mark.parametrize(
        "test_collection,query", 
        [
            (
                TEST_COLLECTION,
                {"board": {'$type': 'string'}}
            )
        ]
    )
    async def test_assert_board_is_string(
        self,
        test_collection,
        query
        ):
        q = db[test_collection].find(query, {'_id': 0, 'board': 1})
        result = [isinstance(i['board'], str) async for i in q]
        assert all(result), 'board is not string'


    @pytest.mark.parametrize(
        "test_collection,query", 
        [
            (
                TEST_COLLECTION,
                {"board": {'$type': 'array'}}
            )
        ]
    )
    async def test_assert_board_not_list(
        self,
        test_collection,
        query
        ):
        q = db[test_collection].find(query, {'_id': 0, 'board': 1})
        result = [i async for i in q]
        assert not result, 'board is not an empty list'