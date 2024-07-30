from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"+-------+-------+-------+\n\
|       |       |       |\n\
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n\
|       |       |       |\n\
+-------+-------+-------+\n\
|       |       |       |\n\
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n\
|       |       |       |\n\
+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    if not game_over:
        accept_move = False
        while not accept_move:
            try:
                move = int(input('Enter your move: '))
                for row in board:
                    for column in row:
                        if column == move:
                            row[row.index(column)] = player_sign
                            accept_move = True
                if not accept_move:
                    print("Invalid cell number")
            except ValueError:
                print("You didn't enter a cell number. (by number)")
                
            
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_cells
    free_cells =[]
    for row in board:
        for column in row:
            if column != player_sign and column != comp_sign:
                free_cells.append((board.index(row), row.index(column)))


def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    global game_over
    if not game_over:
        win = "\nYou win!\n"
        lose = "\nYou lose!\n"
        
        if board[0][1] == board[1][1] == board[2][1] or\
            board[1][0] == board[1][1] == board[1][2] or\
            board[0][0] == board[1][1] == board[2][2] or\
            board[0][2] == board[1][1] == board[2][0] :
            display_board(board)
            game_over = True
            if board[1][1] == player_sign:
                print(win)
            else:
                print(lose)


        elif board[0][0] == board[0][1] == board[0][2] or\
            board[0][0] == board[1][0] == board[2][0]:
            display_board(board)
            game_over = True
            if board[0][0] == player_sign:
                print(win)
            else:
                print(lose)


        elif board[0][2] == board[1][2] == board[2][2] or\
            board[2][0] == board[2][1] == board[2][2]:
            display_board(board)
            game_over = True
            if board[2][2] == player_sign:
                print(win)
            else:
                print(lose)
            
            
        elif len(free_cells) == 0:
            display_board(board)
            print("\nStalemate\n")
            game_over = True



def draw_move(board):
    # The function draws the computer's move and updates the board.
    if not game_over:
        choose_cell = free_cells[randrange(len(free_cells))]
        comp_move = board[choose_cell[0]][choose_cell[1]]
        print("Compuetr`s move: ", comp_move)

        board[choose_cell[0]][choose_cell[1]] = comp_sign


def start_game():
    #The function allows to choose the sing
    global player_sign
    global comp_sign
    global start_board
    global board
    global game_over 
    game_over= False
    accept_sign = False
    sign_x = ["x", "crosses", "cross", "ex", "ex mark", "ex sign", "ex symbol", "ex character", "times", "times sign", "times symbol", "multiplication sign"]
    sign_0 = ["o", "zero", "nought", "nil", "null", "naught", "cipher", "oh", "nul"]

    while not accept_sign:
            player_sign = input("Do you want to be 'X' or '0' :\n")
            if player_sign.lower() in sign_x:
                player_sign = 'X'
                comp_sign = '0'
                accept_sign = True
                start_board= [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            elif player_sign == '0':
                comp_sign = 'X'
                accept_sign = True
                start_board= [
                    [1, 2, 3],
                    [4, "X", 6],
                    [7, 8, 9]
                ]
            elif player_sign.lower() in sign_0:
                comp_sign = 'X'
                player_sign = '0'
                accept_sign = True
                start_board= [
                    [1, 2, 3],
                    [4, "X", 6],
                    [7, 8, 9]
                ]
            else:
                print("\nYou must choose only noughts or crosses.\n")
    board = [row[:] for row in start_board]


def offer_to_play_again(game_over):
    yes = [
    "da",
    "tak",
    "+",
    "y",
    "yes",
    "yup",
    "yeah",
    "yep",
    "sure",
    "sure thing",
    "absolutely",
    "absolutely",
    "totally",
    "totally",
    "definitely",
    "defo",
    "of course",
    "ofc",
    "ofcs",
    "for sure",
    "for sure",
    "you bet",
    "you got it",
    "without a doubt",
    "most definitely"
]
    no = [
    "ne",
    "net",
    "ni",
    "nit",
    "-",
    "n",
    "no",
    "not",
    "nope",
    "nah",
    "not really",
    "not at all",
    "sorry, no",
    "sorry, nope",
    "unfortunately no",
    "unfortunately not",
    "never",
    "definitely not",
    "absolutely not",
    "close",
    "exit",
    "finish",
    "goodbye",
    "farewell",
    "bye",
    "see you later",
    "take care"
]
    if game_over:
        accept_ans = False
        while not accept_ans:
            print("Do you want to play again?:")
            ans = input()
            if ans.lower() in yes:
                accept_ans = True
                game_over = False
                start_game()
            elif ans.lower() in no:
                accept_ans = True
                print("\nOK. Goodbye!\n")
            else:
                print("\nSorry, I don't understend. So..." )


   
print()
start_game()    

print("\nTo make your move enter the cell number\n")
while not game_over:
    display_board(board)
    enter_move(board)
    make_list_of_free_fields(board)
    victory_for(board)
    draw_move(board)
    make_list_of_free_fields(board)
    victory_for(board)
    offer_to_play_again(game_over)
                