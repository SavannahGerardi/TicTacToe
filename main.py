#vars 
player_one_wins = 0
player_two_wins = 0

user_input="yes"

gameboard=[["","",""],["","",""],["","",""]]
currentPlayer = "X"
winner = None
gamerunning = True

def print_board(board):
    print('┌───┬───┬───┐')
    for i, row in enumerate(board):
        print('│ ' + ' │ '.join(row) + ' │')
        if i < 2:
            print('├───┼───┼───┤')
    print('└───┴───┴───┘')


#code if playing alone
if user_input == "alone":
    print("you chose alone")

#code if playing together
if user_input == "with friends":
    print("you chose with friends")

#code if game over


#code who won/lost
def checkhorizontle(gameboard):
    global winner
    if gameboard[0][0] == gameboard[0][1] == gameboard[0][2] and gameboard[0][2] != "":
        print("winner")



#ask user if they are playing alone or with another person
user_input=input("would you like to play? Alone or with a friend?")

checkhorizontle(gameboard)