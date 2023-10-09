from ..conftest import *
# from bson import ObjectId
from pymongo import ReplaceOne
# async def test_update_chan():
        # print('matched: ', update.matched_count)
        # print('modified: ', update.modified_count)
        # print('delete count: ', delete.deleted_count)
        # query = {"board": {"$exists": True}}
        # query = {'board': Board.pol.value}
        # query = {"board": 'pol'}

    # update = await db['4chan'].update_many(
    #     {"board": {"$ne": "pol" }}, 
    #     {'$push': {'board': Board.pol}},
    #     upsert=True
    # )
    # update = await db['4chan'].update_many(
    #     # {"board": {'$type': 'string'}},
    #     # {'board': 'pol'},
    #     {'$push': {'board': Board.pol}},
    #     # upsert=True,
    #     bypass_document_validation=True
    # )
    # delete = await db['4chan'].delete_many({"board": {'$type': 'string'}})
    # pass

TEST_COLLECTION: str = '4chan_test_collection'

@pytest.mark.asyncio
class TestWorker:

    async def test_replace_chan(self):
        data = get_catalog(Board.pol)
        update = []
        for catalog_model in data:
            update.append(ReplaceOne(
                {'no': catalog_model.no}, catalog_model.dict(), upsert=True)
            )
        assert len(update) >= 10, f'check update list len: {update}'
        # pprint(update[:1])
        return update


    async def test_insert_chan(self,):
        update = await self.test_replace_chan()

        idx = await mon_db.create_unique_idx(db[TEST_COLLECTION], 'no')
        assert idx is not None, f'create_unique_idx is None: {idx}'

        result = await db[TEST_COLLECTION].bulk_write(update)
        assert result is not None, f'result is none'
        # assert result.bulk_api_result['nModified'] > 0, 'none modified'
        assert result.bulk_api_result['writeErrors'] == [], 'has errors'
        assert result.bulk_api_result['writeConcernErrors'] == [], 'has write concerns'
        print('')
        print('nModified: ', result.bulk_api_result['nModified'])
        print('nUpserted: ', result.bulk_api_result['nUpserted'])
        print('nInserted: ', result.bulk_api_result['nInserted'])
        print('nRemoved: ', result.bulk_api_result['nRemoved'])
        print('nMatched: ', result.bulk_api_result['nMatched'])
        print('upserted: ', result.bulk_api_result['upserted'])


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