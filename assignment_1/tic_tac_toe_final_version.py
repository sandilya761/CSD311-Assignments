import random

# x or O is used to mark the position on the board
plays = ['X','O']

# Using a standard notion for our playing environment
game_board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
# Magic square for the algorithm to use it for getting the new move and we have used it in a way to have a dual puropose of keeping track of open spaces for input
magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
# variables to help with keeping count of lost and drawn games
lost = 0
draw = 0

# human_list and computer_list are two lists which stores the inputs of human and computer respectively
human_list = []
computer_list = []

#prints the game board and the inner workings of algorithm
def print_gameboard(game_board,human_list,computer_list):
    print("   0,    1,    2")
    for count, row in enumerate(game_board):
        print(count, row)   
    print(human_list)
    print(computer_list)

# pairs list function starts by pairing all sorts of permutaions and checks the sum of pairs and compute the difference between 15 and sum of list pair elements

def pairs(list):
    pairs = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=j:
                D = 15 - (list[i] + list[j])
                if D>0 and D<=9:
                    pairs.append(D)
    return pairs

# tekes human input where human provide rows and columns position
def human_input(magic_square, game_board,plays, human_list, computer_list):
    hrows = int(input("Enter the rows postion for your turn "))
    hcols = int(input("Enter the cols postion for your turn "))
    human_list.append(magic_square[hrows][hcols])
    magic_square[hrows][hcols] = 0
    game_board[hrows][hcols] = plays
    return game_board

pairs_sum = [] 
k = 0

# prints the game board      
def print_square(game_board):
    print("    0    1    2")
    for count, row in enumerate(game_board):
        print(count, row)

# checks the possibility of winning the game and places position accordingly where all the winning positions are calculated using loops 
 
def check_win(game_board):
    # all three rows check
    for i in range(3):
            if game_board[i][0] == game_board[i][1] == game_board[i][2] != '-' :
                print("winner -", game_board[i][0])
                return True
    
    # all three column check
    for j in range(3):
            if game_board[0][j] == game_board[1][j] == game_board[2][j] != '-':
                print("winner |", game_board[0][j])
                return True
               
    # left diagonal
    if game_board[0][0] != '-' and  game_board[0][0] == game_board[1][1] == game_board[2][2]:
        print("winner", game_board[0][0])
        return True

    # right diagonal
    if game_board[0][2] != '-' and  game_board[2][0] == game_board[1][1] == game_board[0][2]:
        print("winner", game_board[2][0])
        return True

# gives the computer input and uses pairs to have the best move possible where using if operator it blocks the specified input after assigning

def computer_input(magic_square, game_board, plays,human_list, computer_list):
    pairs_sum = pairs(computer_list)
    for x in pairs_sum:
        for i in range(3):
            for j in range(3):
                if x == magic_square[i][j]:
                    computer_list.append(x)
                    game_board[i][j] = plays
                    return game_board

    pairs_sum = pairs(human_list)
    for x in pairs_sum:
        for i in range(3):
            for j in range(3):
                if x == magic_square[i][j]:
                    computer_list.append(x)
                    magic_square[i][j] = 0
                    game_board[i][j] = plays
                    
                    return game_board
# computer places random integers in the board for first two turns
    while True:
            crows = random.randint(0,2)
            ccols = random.randint(0,2)
            if magic_square[crows][ccols] != 0:
                computer_list.append(magic_square[crows][ccols])
                game_board[crows][ccols] = plays
                magic_square[crows][ccols] = 0
                
                return game_board

# main function which comprises of all the functions where it has a recursive abilities to let player have choice to play again, and have a look on scoreboard 

def game(magic_square, game_board,plays, human_list, computer_list, draw, lost):
    game_board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

    magic_square = [[8, 3, 4],
                    [1, 5, 9],
                    [6, 7, 2]]
    # human_list and computer_list are two lists which stores the inputs of human and computer respectively
    human_list = []
    computer_list = []
    print("WELCOME TO TIC-TAC-TOE")
    print_square(game_board)
    coin = ['heads', 'tails']
    call = []
    call = input("choose heads or tails: ")
    i = 0   # counter which keeps track of number of turns played by the players
    
    # Toss is used which contains random function  is initited to decide who has to play first
    if random.choice(coin) == call:
        print("you won the toss")
        print("Want to play first? ")
        a= input("Y or N: ")
        # Winning toss and going first, you get to play as x as per the rules of tic tac toe
        if a == 'Y':
            while True:
                print("It's your turn, Enter the rows and columns coordinates: ")
                print()
                game_board = human_input(magic_square, game_board, plays[0], human_list, computer_list)
                i = i+1
                print_gameboard(game_board,human_list,computer_list)
                
                #  when all the grids are filled in the game board and it's a draw 
                if i == 9:
                    print("The game is a draw!")
                    draw = draw + 1
                    print("Drawed games: ", draw, "lost games: ", lost)
                    replay = input("If you want to play again press Y else N")
                    if replay == 'Y':
                        game(magic_square, game_board,plays, human_list, computer_list,draw,lost)
                    break
                print("computer's turn")
                print()
                game_board = computer_input(magic_square, game_board,plays[1] ,human_list, computer_list)
                print_gameboard(game_board,human_list,computer_list)
                i = i + 1
                if check_win(game_board):
                    print("you lost the game.")
                    lost = lost + 1
                    print("Drawed games: ", draw, "lost games: ", lost)
                    replay = input("If you want to play again press Y else N: ")
                    # replay function starts a new game again
                    
                    if replay == 'Y':
                        game(magic_square, game_board,plays, human_list, computer_list, draw, lost)
                    break
                
        else:
            print("You choose not to play first so, computer makes the first move")
            while True:
                print("computers turn")
                game_board = computer_input(magic_square, game_board,plays[0], human_list, computer_list)
                i = i+1
                print_gameboard(game_board,human_list,computer_list)
                if check_win(game_board):
                    print("you lost the game.")
                    lost = lost + 1
                    print("Drawed games: ", draw, "lost games: ", lost)
                    replay = input("If you want to play again press Y else N: ")
                    if replay == 'Y':
                        game(magic_square, game_board,plays, human_list, computer_list,draw,lost)
                        
                    break                        
                if i == 9:    # when all the grids are filled in the game board and it's a draw 
                     print("The game is a draw!")
                     draw = draw + 1
                     print("Drawed games: ", draw, "lost games: ", lost)
                     replay = input("If you want to play again press Y else N: ")
                     if replay == 'Y':
                        game(magic_square, game_board,plays, human_list, computer_list,draw,lost)
                        break
                    
                    
                print("human's turn")
                print()
                game_board = human_input(magic_square, game_board,plays[1], human_list, computer_list)
                
                print_gameboard(game_board,human_list,computer_list)
                i = i + 1
                
    else:  # if human looses the toss computer will get the turn first
        print("you lose the toss")
        print("computer will play first and you will be using o")
        while True:
                print("computers turn")
                game_board = computer_input(magic_square, game_board,plays[0], human_list, computer_list)
                i = i+1
                print_gameboard(game_board,human_list,computer_list)
                if check_win(game_board):
                    print("you lost the game.")
                    lost = lost + 1
                    print("Drawed games: ", draw, "lost games: ", lost)
                    replay = input("If you want to play again press Y else N: ")
                    if replay == 'Y':
                        game(magic_square, game_board,plays, human_list, computer_list, draw, lost)
                    break
                if i == 9:    # when all the grids are filled in the game board and it's a draw
                    print("The game is a draw!")
                    draw = draw + 1
                    print("Drawed games: ", draw, "lost games: ", lost)
                    replay = input("If you want to play again press Y else N: ")
                    if replay == 'Y':
                        game(magic_square, game_board,plays, human_list, computer_list, draw, lost)
                    break  
                
                print("human's turn")
                print()
                game_board = human_input(magic_square, game_board,plays[1], human_list, computer_list)
                print_gameboard(game_board,human_list,computer_list)
                i = i + 1
                 
game(magic_square, game_board, plays,human_list, computer_list, draw, lost)  # main function of the code
