import random
#initially the game board is empty and all the positions are declared as zero.

game_board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
# A sample magic square is declared for verifying the positions. 

magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
# two empty lists are declared for human and computer to keep track of their moves

human_list = []
computer_list = []

# check rows function checks whether the sum of the elements in a row of the game board is 15 

def checkRows(game_board):
    check = 0
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == 0:
                return False
            else:
                check = check + game_board[i][j]
        if check != 15:
            return False    
        check = 0
    return True

# checkcols function checks whether the sum of the elements in a column of the game board is 15 

def checkCols(game_board):
    check = 0
    for i in range(3):
        for j in range(3):
            if game_board[j][i] == 0:
                return False
            else:
                check = check + game_board[j][i]
        if check != 15:
            return False    
        check = 0
    return True

# chechDiagsleft function checks whether the sum of the elements in the left diagonal of the game board is 15

def checkDiagsleft(game_board):
    check = 0
    for i in range(3):
        if game_board[i][i] == 0:
            return False
        else:
            check = check + game_board[i][i]
    if check != 15:
        return False
    return True

# checkDiagsright function whether the sum of the elements in right diagonal of the game board is 15

def checkDiagsright(game_board):
    check = 0
    for i in range(0,3):
        j = 2 - i
        if game_board[i][j] == 0:
            return False
        else:
            check = check + game_board[i][j]
    if check != 15:
        return False    
    return True

# toss function decides whether human starts playing first or computer  

def toss():
    coin = ['heads', 'tails']
    call = []
    call = input("choose heads or tails ")
    print()
    if random.choice(coin) == call:
        print("you won the toss")
    else:
        print("you lose the toss")

# In human_input function the human player gives input as rows and columns in which he has to place his coin

def human_input(magic_square, game_board):
    hrows = input("Enter the rows postion for your turn ")
    hcols = input("Enter the cols postion for your turn ")
    human_list.append(magic_square[hrows][hcols])
    game_board[hrows][hcols] = 1
def computer_input(magic_square, game_board):
    if not computer_list:
        while True:
            crows = random.randint(0,2)
            ccols = random.randint(0,2)
            if magic_square[crows][ccols] not in human_list:
                break
