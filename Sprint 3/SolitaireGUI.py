import tkinter as tk
from tkinter import messagebox, filedialog
from EnglishBoard import EnglishBoard
from GameController import GameController

class SolitaireGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Peg Solitaire - Sprint 3")
        self.board = EnglishBoard(7)
        self.controller = GameController(self.board)
        
        self.selected_peg = None
        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="New Game", command=self.reset_game).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Autoplay Step", command=self.autoplay_step).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Save Game", command=self.save_game).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Load & Replay", command=self.load_game).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        state = self.board.get_state()
        for (x, y), val in state.items():
            if val != -1:
                cx, cy = x * 50 + 40, y * 50 + 40
                color = "blue" if val == 1 else "lightgray"
                if self.selected_peg == (x, y):
                    color = "orange"
                self.canvas.create_oval(cx-18, cy-18, cx+18, cy+18, fill=color)

    def handle_click(self, event):
        x, y = (event.x - 40) // 50, (event.y - 40) // 50
        state = self.board.get_state()
        if (x, y) in state and state[(x, y)] != -1:
            if self.selected_peg is None:
                if state[(x, y)] == 1:
                    self.selected_peg = (x, y)
            else:
                success = self.controller.make_manual_move(self.selected_peg, (x, y))
                self.selected_peg = None
                if success and self.controller.check_game_over():
                    messagebox.showinfo("Game Over", "No more valid moves!")
            self.draw_board()

    def autoplay_step(self):
        self.controller.execute_automated_step()
        self.draw_board()

    def reset_game(self):
        self.board.initialize_board()
        self.selected_peg = None
        self.draw_board()

    def save_game(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            self.controller.recorder.save_to_file(path)
            messagebox.showinfo("Saved", "Game saved successfully!")

    def load_game(self):
        path = filedialog.askopenfilename(defaultextension=".txt")
        if path:
            try:
                # 1. Load the move history from file
                moves = self.controller.recorder.load_from_file(path)
                
                # 2. Reset the board back to the initial starting layout
                self.board.initialize_board()
                self.selected_peg = None
                
                # 3. Replay each recorded move onto the board
                for start, end in moves:
                    self.controller.make_manual_move(start, end)
                
                # 4. Refresh the GUI canvas to show the replayed state
                self.draw_board()
                messagebox.showinfo("Replay", "Game loaded and replayed successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load game: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SolitaireGUI(root)
    root.mainloop()