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


