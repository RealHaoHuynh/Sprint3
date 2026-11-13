class GameRecorder:
    def __init__(self):
        self._move_history = []

    def record_move(self, start_pos: tuple, end_pos: tuple):
        self._move_history.append((start_pos, end_pos))

    def save_to_file(self, filepath: str):
        with open(filepath, 'w') as f:
            for move in self._move_history:
                f.write(f"{move[0][0]},{move[0][1]} -> {move[1][0]},{move[1][1]}\n")

    def load_from_file(self, filepath: str) -> list:
        self._move_history = []
        with open(filepath, 'r') as f:
            for line in f:
                if " -> " not in line:
                    raise ValueError("Corrupted log file format")
                parts = line.strip().split(" -> ")
                start = tuple(map(int, parts[0].split(',')))
                end = tuple(map(int, parts[1].split(',')))
                self._move_history.append((start, end))
        return self._move_history