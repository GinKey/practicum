import tkinter as tk
import random

EMPTY = ""
PLAYER_X = "X"
PLAYER_O = "O"
BOARD_SIZE = 3

board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

player_turn = True
game_over = False


def check_win(player):
    for i in range(BOARD_SIZE):
        if all([board[i][j] == player for j in range(BOARD_SIZE)]):
            return True

    for j in range(BOARD_SIZE):
        if all([board[i][j] == player for i in range(BOARD_SIZE)]):
            return True

    if all([board[i][i] == player for i in range(BOARD_SIZE)]):
        return True
    if all([board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)]):
        return True

    return False


def computer_move():
    global player_turn, game_over

    empty_cells = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == EMPTY]

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = PLAYER_O
        if check_win(PLAYER_O):
            game_over = True
        player_turn = True
    if not empty_cells:
        print("Ничья")
        game_over = True


def player_move(row, col):
    global player_turn, game_over

    if board[row][col] == EMPTY and not game_over:
        board[row][col] = PLAYER_X
        if check_win(PLAYER_X):
            game_over = True
        else:
            computer_move()


def draw_board(canvas):
    canvas.delete("all")
    cell_size = 100
    margin = 10

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x1 = col * cell_size + margin
            y1 = row * cell_size + margin
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2)

            if board[row][col] == PLAYER_X:
                x1 += cell_size * 0.2  # Увеличение размера крестика
                y1 += cell_size * 0.2
                x2 = x1 + cell_size * 0.6
                y2 = y1 + cell_size * 0.6
                canvas.create_line(x1, y1, x2, y2)
                canvas.create_line(x1, y2, x2, y1)

            elif board[row][col] == PLAYER_O:
                x1 += cell_size * 0.1
                y1 += cell_size * 0.1
                x2 = x1 + cell_size * 0.8
                y2 = y1 + cell_size * 0.8
                canvas.create_oval(x1, y1, x2, y2)


    if game_over:
        if check_win(PLAYER_X):
            winner = PLAYER_X
            message = f"{winner} победил!"
        elif check_win(PLAYER_O):
            winner = PLAYER_O
            message = f"{winner} победил!"
        else:
            message = f"Ничья!"

        toplevel = tk.Toplevel()
        toplevel.geometry("200x50+200+100")
        toplevel.overrideredirect(True)
        toplevel.configure(bg='white')
        label = tk.Label(toplevel, text=message, font=("Arial", 16), bg="white")
        label.pack(fill='both', expand=True)

def handle_click(event):
    global player_turn
    if player_turn:
        row = int(event.y / 100)
        col = int(event.x / 100)
        player_move(row, col)
        draw_board(canvas)

root = tk.Tk()
root.title("Крестики-нолики")

canvas = tk.Canvas(root, width=BOARD_SIZE * 105, height=BOARD_SIZE * 105)
canvas.pack()

canvas.bind("<Button-1>", handle_click)

draw_board(canvas)

root.mainloop()

