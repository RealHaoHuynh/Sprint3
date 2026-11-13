import random
from GameRecorder import GameRecorder

class GameController:
    def __init__(self, board):
        self.board = board
        self.recorder = GameRecorder()
        self.is_automated = False

    def make_manual_move(self, start: tuple, end: tuple) -> bool:
        if self.board.is_valid_jump(start, end):
            self.board.update_cell(start[0], start[1], 0)
            mid_x = (start[0] + end[0]) // 2
            mid_y = (start[1] + end[1]) // 2
            self.board.update_cell(mid_x, mid_y, 0)
            self.board.update_cell(end[0], end[1], 1)
            self.recorder.record_move(start, end)
            return True
        return False

    def execute_automated_step(self) -> bool:
        valid_moves = self.board.get_valid_moves()
        if not valid_moves:
            return False
        start, end = random.choice(valid_moves)
        return self.make_manual_move(start, end)

    def check_game_over(self) -> bool:
        return len(self.board.get_valid_moves()) == 0

    def randomize_board_state(self):
        pegs = [k for k, v in self.board.get_state().items() if v != -1]
        random.shuffle(pegs)
        state = self.board.get_state()
        for k in state:
            if state[k] != -1:
                state[k] = 0
        for i in range(len(pegs) // 2):
            self.board.update_cell(pegs[i][0], pegs[i][1], 1)