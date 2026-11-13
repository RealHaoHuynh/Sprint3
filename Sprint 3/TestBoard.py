import unittest
from EnglishBoard import EnglishBoard
from DiamondBoard import DiamondBoard

class TestBoard(unittest.TestCase):
    def test_board_type_selection(self):
        board = EnglishBoard(7)
        self.assertIsNotNone(board.get_state())

    def test_board_dimension_initialization(self):
        board = DiamondBoard(5)
        state = board.get_state()
        self.assertIn((2, 2), state)

    def test_randomize_state(self):
        board = EnglishBoard(7)
        initial_pegs = sum(1 for v in board.get_state().values() if v == 1)
        self.assertGreater(initial_pegs, 0)

if __name__ == "__main__":
    unittest.main()