from tests.conftest import *
from time import sleep

class Test_Chan_Images:

    folder_path = './chan_images'

    @pytest.mark.parametrize(
        "board", 
        [
            (
                Board.pol 
            ),
            (
                Board.wg 
            ),
            (
                Board.hr 
            )
        ]
    )
    def test_assert_board_is_string(self, board):
        sleep(3)
        iter_img_lst(board, self.folder_path)


