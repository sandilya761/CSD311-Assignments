import random
game_board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]

human_list = []
computer_list = []

def print_gameboard(game_board):
    print("   0, 1, 2")
    for count, row in enumerate(game_board):
        print(count, row)   

def pairs(list):
    pairs = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=j:
                D = 15 - (list[i] + list[j])
                if D>0 and D<9:
                    pairs.append(D)
    return pairs

def human_input(magic_square, game_board, human_list, computer_list):
    hrows = int(input("Enter the rows postion for your turn "))
    hcols = int(input("Enter the cols postion for your turn "))
    human_list.append(magic_square[hrows][hcols])
    magic_square[hrows][hcols] = 0
    game_board[hrows][hcols] = 1
    return game_board

pairs_sum = [] 
k = 0
def computer_input(magic_square, game_board, human_list, computer_list, k):
    pairs_sum = pairs(human_list)
    for x in pairs_sum:
        for i in range(3):
            for j in range(3):
                if x == magic_square[i][j]:
                    computer_list.append(x)
                    magic_square[i][j] = 0
                    game_board[i][j] = 2
                    k = 0
                    return game_board, k

    pairs_sum = pairs(computer_list)
    for x in pairs_sum:
        for i in range(3):
            for j in range(3):
                if x == magic_square[i][j]:
                    computer_list.append(x)
                    game_board[i][j] = 2
                    print("Winner Bro")
                    k = 1
                    return game_board, k
    while True:
            crows = random.randint(0,2)
            ccols = random.randint(0,2)
            if magic_square[crows][ccols] != 0:
                computer_list.append(magic_square[crows][ccols])
                game_board[crows][ccols] = 2
                magic_square[crows][ccols] = 0
                k = 0
                return game_board, k

def game(magic_square, game_board, human_list, computer_list, k):
    while True:
        game_board = human_input(magic_square, game_board, human_list, computer_list)
        print_gameboard(game_board)
        game_board, k = computer_input(magic_square, game_board, human_list, computer_list, k)
        print_gameboard(game_board)
        if k != 0:
            print("you lose you fucking loser")
            break
game(magic_square, game_board, human_list, computer_list, k)
