#Create the game board
#I am going to create a dictionary mapped with the numpad keys so players can use those as inputs for the game
theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

#This function will take the keys from the dictionary above and map them to the places on the tictactoe board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#Now that there is a game board we need to move on to the funcitonality of the game itself
#which involves taking input from the player and assigning it to a position on the board 
# as well as performing checks to see if the game has been won or not
def game():
    #assign the initial player
    player = 'X'
    #create a turn counter
    count = 0
    for i in range(10):
        print("Player " + player + "'s turn. Make your move.")
        printBoard(theboard)
        move = int(input())
        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That move is invalid. Try again.")
            continue
        



print(theboard[8])
game()
