# define the board
board = [' ' for _ in range(9)]

# function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# function to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# function to check for a draw
def check_draw():
    return all(space != ' ' for space in board)

# minimax algorithm
def minimax(is_maximizing):
    if check_win('O'):
        return 1
    if check_win('X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
# function for AI move
def ai_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player move
        while True:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                if board[player_move] == ' ':
                    board[player_move] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except (IndexError, ValueError):
                print("Please enter a number between 1 and 9.")

        print_board()

        if check_win('X'):
            print("Congratulations! You win!")
            break
        if check_draw():
            print("It's a draw!")
            break

        # AI move
        ai_move()
        print("AI has made its move:")
        print_board()

        if check_win('O'):
            print("AI wins! Better luck next time.")
            break
        if check_draw():
            print("It's a draw!")
            break
if __name__ == "__main__":
    main()
# end of the game loop
# run the game
