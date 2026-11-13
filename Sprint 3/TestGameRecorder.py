import unittest
from EnglishBoard import EnglishBoard
from GameController import GameController

class TestGameController(unittest.TestCase):
    def setUp(self):
        self.board = EnglishBoard(7)
        self.controller = GameController(self.board)

    def test_valid_manual_move(self):
        # Standard opening jump on English board: (3,1) to (3,3) over (3,2)
        success = self.controller.make_manual_move((3, 1), (3, 3))
        self.assertTrue(success)
        self.assertEqual(self.board.get_state()[(3, 1)], 0)
        self.assertEqual(self.board.get_state()[(3, 3)], 1)

    def test_mode_switching(self):
        self.controller.is_automated = True
        self.assertTrue(self.controller.is_automated)

    def test_automated_move_execution(self):
        move_made = self.controller.execute_automated_step()
        self.assertTrue(move_made)

    def test_game_over_detection(self):
        is_over = self.controller.check_game_over()
        self.assertFalse(is_over)

if __name__ == "__main__":
    unittest.main()