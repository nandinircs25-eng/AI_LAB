
import random

# Create the board
board = [' ' for _ in range(9)]


# Display the board
def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


# Check whether a player has won
def check_win(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check whether the board is full
def is_draw():
    return ' ' not in board


# Computer's move
def computer_move():
    empty_cells = [i for i in range(9) if board[i] == ' ']

    if empty_cells:
        position = random.choice(empty_cells)
        board[position] = 'O'


# Main game
print("TIC-TAC-TOE")
print("HUMAN = X")
print("COMPUTER = O")

while True:
    display_board()

    # Human's turn
    try:
        position = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if position < 0 or position > 8:
        print("Invalid position! Choose between 1 and 9.")
        continue

    if board[position] != ' ':
        print("That position is already occupied!")
        continue

    board[position] = 'X'

    # Check human win
    if check_win('X'):
        display_board()
        print("HUMAN WINS!")
        break

    # Check draw
    if is_draw():
        display_board()
        print("GAME DRAW!")
        break

    # Computer's turn
    computer_move()
    print("Computer has made its move.")

    # Check computer win
    if check_win('O'):
        display_board()
        print("COMPUTER WINS!")
        break

    # Check draw
    if is_draw():
        display_board()
        print("GAME DRAW!")
        break

