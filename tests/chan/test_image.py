from ..conftest import *

# @pytest.mark.asyncio
class Test_Chan_Images:
    # @pytest.mark.parametrize(
    #     "test_collection,query", 
    #     [
    #         (
    #             _test_collection,
    #             {"board": {'$type': 'string'}}
    #         )
    #     ]
    # )
    def test_assert_board_is_string(self):
        # iter_img_lst(Board.wg, './chan_images')
        # iter_img_lst(Board.pol, './chan_images')
        iter_img_lst(Board.hr, './chan_images')


