import random
from re import X

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 
# 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3])
    
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.

def player_input():
    player1_marker = "Wrong"
    acceptable_value = ["X", "O"]
    
    while player1_marker not in acceptable_value:
        
       player1_marker = input("Player 1: Would you like to be X or O?: ")
       if player1_marker not in acceptable_value:
           print("Sorry, Invalid Input. Please enter X or O")
           
    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
        player1_marker = "O"
        
    return (player1_marker,player2_marker)
       
# (player1,player2) = player_input();
# print(player1)
# print(player2)
    
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired
# position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[int(position)] = marker;
    return board;

# place_marker(test_board,'$',8)
# display_board(test_board)

# *Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    # Checking Horizontal Win Conditions
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    # Checking Vertical Win Conditions
    elif board[7] == mark and board[4] == mark and board[1] == mark:
            return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    # Checking Diagonal Win Conditions
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    else:
        return False

# test_board = ['#','X','X','X','O','X','O','X','O','X']
# Result = win_check(test_board,"X")
# if result:
#     print("You Won")

# Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.
def choose_first():
    random_value = random.randint(0,1)
    if random_value == 0:
        return "Player 1 goes first"
    else:
        return "Player 2 goes first"
    
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):  
    currently_Occupied = ["X","O"]
    return board[position] not in currently_Occupied

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# result = space_check(test_board,1)
# if result:
#     print("not occupied")
# else:
#     print("Occupied")

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for space in board:
        if space != "X" and space != "O" and space != "#":
            return False
    return True

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# result = full_board_check(test_board)
# if result:
#     print("Full")
# else:
#     print("Not Full")

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from 
# step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    player_decision = "Wrong"
    space_availiable = False
    acceptable_values = range(1,10)
    
    while player_decision.isdigit() == False or space_availiable == False:
        player_decision = input("Where do you want to place your marker? Please enter a number from 1-9: ")
        
        if player_decision.isdecimal() == False:
            print("Sorry, you did not enter a digit. Please try again")
        else:
            player_decision = int(player_decision)
        
            if player_decision not in acceptable_values:
                print("Sorry, the value is not in range. Please enter a value between 1-9")
            else:
                ##Check if the space is availiable
                space_availiable = space_check(board, player_decision)
                if space_availiable == False:
                    print("Sorry the space is not availiable.")
                else:
                    space_availiable = True    
                player_decision = str(player_decision)
    return player_decision

# test_board = ['#','J','O','X','O','X','O','X','O','X']
# display_board(test_board)
# result =player_choice(test_board)     
# print(type(result))
            
# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    
    result = "Wrong"
    while result not in ["Y","N"]:
        
        result = input("Do you want to play again? Y or N: ")
    
        if result not in ["Y","N"]:
            print("Sorry, I didn't understand. Please make sure to choose Y or N")
    if result == "Y":
        return True
    else:
        return False
# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
play_game = True
while play_game:
    print('Welcome to Tic Tac Toe!')
    player1_marker, player2_marker = player_input()
    gameon = True
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    while gameon:
        # Player 1 Turn
        print("Player 1's Turn")
        player1_position = player_choice(board)
        # Place the marker
        board = place_marker(board,player1_marker,player1_position)
        display_board(board)
        #Check Win conditions
        victory = win_check(board,player1_marker)
        if victory:
            print("Player 1 Wins!")
            gameon = replay();
            continue
        # Check if board is full
        if full_board_check(board):
            if not victory:
                print("It is a tie")
                gameon = replay();
        
        # Player 2 Turn
        print("Player 2's Turn")
        player2_position = player_choice(board);
        # Place the marker
        board = place_marker(board,player2_marker,player2_position)
        display_board(board)
        #Check Win conditions
        victory = win_check(board,player2_marker)
        if victory:
            print("Player 2 Wins!")
            gameon = replay();
            continue
        # Check if board is full
        if full_board_check(board):
            if not victory:
                print("It is a tie")
                gameon = replay();
    play_game = False;
    
    