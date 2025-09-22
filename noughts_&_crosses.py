import random
import time

# Create board and moves
board = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Display board
def display_board(b):
    for row in b:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|", end="")
        for element in row:
            print(f"   {element}   |", end="")
        print()
        print("|       |       |       |")
    print("+-------+-------+-------+")


# Check for winner
def check_winner(b):
    for row in b:
        if row[0] == row[1] == row[2] and row[0] in ["X", "0"]:
            return row[0]
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] and b[0][col] in ["X", "0"]:
            return b[0][col]
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] in ["X", "0"]:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] in ["X", "0"]:
        return b[0][2]
    return None


# User move
def user_turn(b):
    while True:
        try:
            move = int(input("Your turn. Enter a number between 1 and 9: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        if move in available_moves:
            for i in range(3):
                for j in range(3):
                    if b[i][j] == move:
                        b[i][j] = "X"
                        available_moves.remove(move)
                        return
        else:
            print("Invalid or taken move. Try again.")


# Computer move
def computer_turn(b):
    move = random.choice(available_moves)
    print(f"Opponent's turn. They chose: {move}")
    available_moves.remove(move)
    for i in range(3):
        for j in range(3):
            if b[i][j] == move:
                b[i][j] = "0"
                return


# Main game
def game():
    print("NOUGHTS & CROSSES!")
    time.sleep(1.0)
    display_board(board)

    while True:
        user_turn(board)
        display_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{'You' if winner == 'X' else 'Opponent'} win!")
            break
        if not available_moves:
            print("It's a draw!")
            break

        time.sleep(1.0)
        computer_turn(board)
        display_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{'You' if winner == 'X' else 'Opponent'} win!")
            break
        if not available_moves:
            print("It's a draw!")
            break


game()
