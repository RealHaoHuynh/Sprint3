from Board import Board

class DiamondBoard(Board):
    def initialize_board(self):
        n = self._size
        center = n // 2
        for x in range(n):
            for y in range(n):
                if abs(x - center) + abs(y - center) <= center:
                    self._board_state[(x, y)] = 1
                else:
                    self._board_state[(x, y)] = -1
        self._board_state[(center, center)] = 0

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