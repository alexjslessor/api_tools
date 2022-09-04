from ..conftest import *


@pytest.mark.asyncio
class Test_MongoDB_Insert:

    async def test_insert_chan(self):
        data = get_catalog(Board.pol)
        update = []
        for catalog_model in data:
            update.append(ReplaceOne(
                {'no': catalog_model.no}, catalog_model.dict(), upsert=True)
            )

        idx = await mon_db.create_unique_idx(db['4chan'], 'no')
        assert idx is not None
        print(idx)
        # assert idx['ok'] == 1
        # assert idx['nIndexesWas'] == 1
        # assert idx['nIndexes'] == 2

        result = await db['4chan'].bulk_write(update)

        assert result is not None
        assert result.bulk_api_result['nModified'] > 0
        assert result.bulk_api_result['writeErrors'] == []
        assert result.bulk_api_result['writeConcernErrors'] == []
        print('nModified: ', result.bulk_api_result['nModified'])
        print('nUpserted: ', result.bulk_api_result['nUpserted'])
        print('nInserted: ', result.bulk_api_result['nInserted'])
        print('nRemoved: ', result.bulk_api_result['nRemoved'])
        print('nMatched: ', result.bulk_api_result['nMatched'])
        print('upserted: ', result.bulk_api_result['upserted'])



        # resp = await db['four_chan'].insert_many((i.dict() for i in data))
        # idx = await mon_db.create_unique_idx(db['four_chan'], 'no')
        # pprint(data)
        # print(resp)
        # print(idx)

        # await mon_db.drop_collection(db, 'four_chan')



    # def test_insert(self):
        # loop = aio.get_or_create_eventloop()
        # loop.run_until_complete(
            # mon_db.insert_many_documents(db, CollectionNames.testing, data)
            # mon_db.insert_docs_test(db, CollectionNames.testing, d)
        # )

        # asyncio.run(db[CollectionNames.testing].insert_docs_test(db, CollectionNames.testing, data))
#     #     # asyncio.run(mon_db.insert_many_documents(db, CollectionNames.testing, data))
#     #     loop.close()

