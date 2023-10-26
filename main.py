#vars 
player_one_wins = 0
player_two_wins = 0

user_input="yes"

gameboard=[["x","o","o"],["x","x","x"],["o","o","x"]]

def print_board(board):
    print('┌───┬───┬───┐')
    for i, row in enumerate(board):
        print('│ ' + ' │ '.join(row) + ' │')
        if i < 2:
            print('├───┼───┼───┤')
    print('└───┴───┴───┘')

#ask user if they are playing alone or with another person
user_input=input("would you like to play? Alone or with a friend?")

#code if playing alone
if user_input == "alone":
    print("you chose alone")

#code if playing together
if user_input == "with friends":
    print("you chose with friends")

#code if game over

#code who won/lost

