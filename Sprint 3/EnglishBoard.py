from Board import Board

class EnglishBoard(Board):
    def initialize_board(self):
        # Standard 7x7 English cross board layout
        # 1 represents a peg, 0 represents empty, -1 represents invalid/out of bounds
        for x in range(7):
            for y in range(7):
                # Cross shape check
                if (2 <= x <= 4) or (2 <= y <= 4):
                    self._board_state[(x, y)] = 1
                else:
                    self._board_state[(x, y)] = -1
        # Center starts empty
        self._board_state[(3, 3)] = 0

    def get_valid_moves(self) -> list:
        moves = []
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        for pos, val in self._board_state.items():
            if val == 1:
                x, y = pos
                for dx, dy in directions:
                    end = (x + dx, y + dy)
                    if self._board_state.get(end) == 0 and self.is_valid_jump(pos, end):
                        moves.append((pos, end))
        return moves