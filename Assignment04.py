#python programming internship at InternPe
#Assignment 1
#implement tic-tac-toe game

def print_board(board):
    print("+-----------+")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + str(board[i][j]) + " ", end="|")
        print("\n+-----------+")

def check_win(board):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != "-") or (board[0][i] == board[1][i] == board[2][i] != "-"):
            return True
    if (board[0][0] == board[1][1] == board[2][2] != "-") or (board[0][2] == board[1][1] == board[2][0] != "-"):
        return True
    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return False
    return True

def play_game():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        row = int(input("Enter row for " + player + " (1-3): "))
        col = int(input("Enter column for " + player + " (1-3): "))
        if board[row-1][col-1] != "-":
            print("That spot is already taken!")
            continue
        board[row-1][col-1] = player
        print_board(board)
        if check_win(board):
            print(player + " wins!")
            break
        if check_tie(board):
            print("Tie!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

while True:
    n=int(input("choose any option:  \n 1.Start \n 2.Exit"))
    if(n==1):
        play_game()
    else:
        print("game exited....")
        break

