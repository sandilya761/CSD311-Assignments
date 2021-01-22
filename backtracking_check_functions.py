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

