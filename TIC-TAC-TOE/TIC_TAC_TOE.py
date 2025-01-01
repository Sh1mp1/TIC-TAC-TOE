import os
import time

def checkWin(board): #Returns the player that has won (-1 for player , -2 for computer)
    #Check each horizontal row
    for i in range(0, 9, 3):
        if (board[i] == board[i + 1] and board[i + 1] == board[i + 2]):
            return board[i]

    #Check each vertical column
    for i in range(0,3):
        if (board[i] == board[i + 3] and board[i + 3] == board[i + 6]):
            return board[i]

    #Check both diagonals
    if (board[0] == board[4] and board[4] == board[8]):
        return board[4]

    if (board[2] == board[4] and board[4] == board[6]):
        return board[4]

    return None

def playerTurn(board):
    
    while (True):
        choice = input("Enter your choice(1 - 9) : ")
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        choice = int(choice)
        if (choice <= 0 or choice >= 10):
            print("Input out of range")
        elif (board[choice - 1] < 1):
            print("Spot already taken")
        else:
            board[choice - 1] = -1
            return None

def computerTurn(board):

    #Find winning move
    for i in range(0, 9):
        #Check for empty space
        if (board[i] == i + 1):
            board[i] = -2       #Assume the bot moves here
            if (checkWin(board) == -2):            
                return
            board[i] = i + 1    #Undo the move

    #Block opponent
    for i in range(0, 9):
        #Check for empty space
        if (board[i] == i + 1):
            board[i] = -1       #Assume the player moves here
            if (checkWin(board) == -1):
                board[i] = -2
                return
            board[i] = i + 1    #Undo the move

    #Takes middle block if empty
    if (board[4] == 5):
        board[4] = -2
        return

    #Takes any corner if empty
    for i in [0, 2, 6, 8]:
        if (board[i] > 0):
            board[i] = -2
            return

    #Takes any empty side
    for i in range(0, 9):
        if (board[i] == i + 1):
            board[i] = -2
            return


def render(board):
    os.system('cls') #Clears the terminal
    for i in range(0, 9):
        if (board[i] > 0):
            print(board[i], end = "")
        elif (board[i] == -1):
            print("X" , end = "")
        elif (board[i] == -2):
            print("O", end = "")
        if (i == 2 or i == 5):
            print() #For a new line
            print("-----------")
            continue
        if (i < 8):
            print(" | ", end = "")

    print()
    print()



#main-------------------------------
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#[1][2][3]
#[4][5][6]
#[7][8][9]
tie = True

for i in range(1, 6):
    render(board)

    playerTurn(board)

    if (checkWin(board) == -1):
        print("YOU WIN!")
        tie = False
        break

    render(board)

    if (i == 5): #All 9 spots taken
        break

    print("COMPUTER'S TURN")

    time.sleep(0.5)

    computerTurn(board)

    render(board)

    if (checkWin(board) == -2):
        print("COMPUTER WINS!")
        tie = False
        break

if (tie):
    print("ITS A DRAW!")

input()