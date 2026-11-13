from abc import ABC, abstractmethod

class Board(ABC):
    def __init__(self, size: int):
        self._size = size
        self._board_state = {}
        self.initialize_board()

    @abstractmethod
    def initialize_board(self):
        """Initialize the peg layout for the board type."""
        pass

    def get_state(self) -> dict:
        """Return a copy of the current board state dictionary."""
        return self._board_state.copy()

    def update_cell(self, x: int, y: int, value: int):
        """Update a specific cell value (0 for empty, 1 for peg)."""
        self._board_state[(x, y)] = value

    @abstractmethod
    def get_valid_moves(self) -> list:
        """Return a list of all valid moves available on the board."""
        pass

    def is_valid_jump(self, start: tuple, end: tuple) -> bool:
        """Validate standard peg jump rules."""
        if self._board_state.get(start) == 1 and self._board_state.get(end) == 0:
            mid_x = (start[0] + end[0]) // 2
            mid_y = (start[1] + end[1]) // 2
            return self._board_state.get((mid_x, mid_y)) == 1
        return False