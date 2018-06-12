# Author: Maude DEROCHE
# Date: 08.06.2018
# Aim: code initiation
# Use: Python 3
# Licence : MIT

# RPSSL : rock, paper, scissors, spock, lizard.

# IMPORT LIBRARIES
##################################
import random as rd

# DECLARE VARIABLES
##################################
TURN = 0
BESTOF = 0
SCOREP1 = 0
SCOREP2 = 0
MOVEP1 = 0
MEMORY = rd.randint(1,5)
MOVEP2 = 0
MOVES = {1:'Paper',2:'Rock',3:'Cisors',4:'Lezard',5:'Spock'} # Dictionary {key1:value1,key2:value2}

# DECLARE FUNCTIONS
#################################

# Cheating IA, playing always best move, after you!
def get_cheat_move_player_2(move):
    # return int move - 1 or 3 if move is 1
    if move == 1:
        return 3
    else:
        return move - 1

# Cheating IA, playing always draw move, after you!
# Fairplay IA, playing always your last move, before you.
def get_copycat_move_player_2(move):
    # return move
    return move

# Fairplay IA, playing random move, before you.
def get_random_move_player_2(move):
    # return random move 
    return rd.randint(1,5)

# User move
def get_move_player_1():
    # ask player 1 move
    global MEMORY
    print("You can play, 1:Paper, 2:Rock, 3:Cisors, 4:Lezard, 5:Spock")
    print ("")
    move = int(input("What is your move? "))
    print("")
    # Check if valide move [1-5]
    while move > 5 or move < 1:
        print("You can play, 1:Paper, 2:Rock, 3:Cisors, 4:Lezard, 5:Spock")
        print ("")
        move = int(input("What is your move? "))
        print("")
    MEMORY = move
    return move

# Who win round
def set_round_winner(move1, move2):
    # determined round winner and increase this score
    global SCOREP2
    global SCOREP1
    if move1 == move2:
        return None
    else:
        if move1 == 1 and (move2 == 3 or move2 == 4):
            SCOREP2 += 1
        elif move1 == 2 and (move2 == 1 or move2 == 5):
            SCOREP2 += 1
        elif move1 == 3 and (move2 == 2 or move2 == 5):
            SCOREP2 += 1
        elif move1 == 4 and (move2 == 2 or move2 == 3):
            SCOREP2 += 1
        elif move1 == 5 and (move2 == 1 or move2 == 4):
            SCOREP2 += 1
        else:        
            SCOREP1 += 1

# Who win game
def get_final_winner(score1, score2):
    if score1 == score2:
        print("DRAW !")
        print ("")
    elif score1 > score2:
        print("You win with a score of", score1, "to", score2, "for me")
        print ("")
    else:
        print("You loose with a score of", score1, "to", score2, "for me")
        print ("")

# GAME
#################################

# INTRO
print ("")
print ("")
print("Welcome in Paper, Rock, Cisors, Lezard, Spock !!!!")
print("")

# How many round(s)
BESTOF = int(input("How many odd round(s) do you want to play? "))
# Check if positive and odd
while BESTOF <= 0 or BESTOF % 2 == 0:
    BESTOF = int(input("How many odd round(s) do you want to play? "))

# LOOP
while TURN < BESTOF:
# Comment / uncomment IA MOVEP2 (here, fairplay IA playing your last move, first random)
    MOVEP2 =  get_copycat_move_player_2(MEMORY)
    #MOVEP2 =  get_random_move_player_2(MEMORY)
    MOVEP1 = get_move_player_1()
    #MOVEP2 = get_cheat_move_player_2(MOVEP1)
    #MOVEP2 = get_copycat_move_player_2(MOVEP1)
    set_round_winner(MOVEP1, MOVEP2)
    TURN += 1
    print ("I played:", MOVES[MOVEP2], "and you played:", MOVES[MOVEP1])
    print ("Score turn:", TURN, "YOU:", SCOREP1, "ME:", SCOREP2)
    print ("")

# FINAL    
get_final_winner(SCOREP1, SCOREP2)

# CLOSE
CLOSE = input("Thanks for playing my game. Press a key to leave. ")
