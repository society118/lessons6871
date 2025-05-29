import tkinter as tk

CELL_SIZE = 30
GRID_WIDTH = 15
GRID_HEIGHT = 15

WALL = "#"
FOOD = "."
EMPTY = " "

# Простий рівень: # - стіни, . - їжа
LEVEL = [
    "###############",
    "#.............#",
    "#.#####.#####.#",
    "#.#...#.#...#.#",
    "#.#.#.#.#.#.#.#",
    "#.............#",
    "###.#.###.#.###",
    "###.#..P..#.###",
    "###.#.###.#.###",
    "#.............#",
    "#.#.#.#.#.#.#.#",
    "#.#...#.#...#.#",
    "#.#####.#####.#",
    "#.............#",
    "###############"
]


class PacmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Пакмен на Tkinter")
        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg="black")
        self.canvas.pack()
        self.grid = []
        self.pacman_pos = (0, 0)
        self.food_count = 0

        self.load_level()
        self.draw_grid()
        self.root.bind("<KeyPress>", self.handle_key)

    def load_level(self):
        for y, row in enumerate(LEVEL):
            grid_row = []
            for x, char in enumerate(row):
                if char == "P":
                    self.pacman_pos = (x, y)
                    grid_row.append(EMPTY)
                else:
                    grid_row.append(char)
                if char == FOOD:
                    self.food_count += 1
            self.grid.append(grid_row)

    def draw_grid(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                if cell == WALL:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                elif cell == FOOD:
                    self.canvas.create_oval(x1 + 12, y1 + 12, x2 - 12, y2 - 12, fill="white", outline="")

        # Намалювати пакмена
        px, py = self.pacman_pos
        x1 = px * CELL_SIZE
        y1 = py * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_oval(x1 + 2, y1 + 2, x2 - 2, y2 - 2, fill="yellow", outline="")

    def handle_key(self, event):
        dx, dy = 0, 0
        if event.keysym == "Up":
            dy = -1
        elif event.keysym == "Down":
            dy = 1
        elif event.keysym == "Left":
            dx = -1
        elif event.keysym == "Right":
            dx = 1

        new_x = self.pacman_pos[0] + dx
        new_y = self.pacman_pos[1] + dy

        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
            target_cell = self.grid[new_y][new_x]
            if target_cell != WALL:
                if target_cell == FOOD:
                    self.food_count -= 1
                    self.grid[new_y][new_x] = EMPTY
                    if self.food_count == 0:
                        self.show_win_message()
                self.pacman_pos = (new_x, new_y)
                self.draw_grid()

    def show_win_message(self):
        self.canvas.create_text(GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2,
                                text="Ти переміг!", fill="white", font=("Arial", 32, "bold"))


if __name__ == "__main__":
    root = tk.Tk()
    game = PacmanGame(root)
    root.mainloop()
