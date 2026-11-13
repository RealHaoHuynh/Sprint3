from Board import Board

class HexagonBoard(Board):
    def initialize_board(self):
        # Simplified hexagonal layout generation based on size radius
        radius = self._size
        for q in range(-radius, radius + 1):
            r1 = max(-radius, -q - radius)
            r2 = min(radius, -q + radius)
            for r in range(r1, r2 + 1):
                self._board_state[(q, r)] = 1
        # Center empty
        if (0, 0) in self._board_state:
            self._board_state[(0, 0)] = 0

    def get_valid_moves(self) -> list:
        moves = []
        hex_directions = [(2, -1), (1, 1), (-1, 2), (-2, 1), (-1, -1), (1, -2)]
        for pos, val in self._board_state.items():
            if val == 1:
                q, r = pos
                for dq, dr in hex_directions:
                    end = (q + dq, r + dr)
                    mid = ((q + end[0]) // 2, (r + end[1]) // 2)
                    if self._board_state.get(end) == 0 and self._board_state.get(mid) == 1:
                        moves.append((pos, end))
        return moves