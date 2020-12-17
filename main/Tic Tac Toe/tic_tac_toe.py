import random
import time

game_board = [' ' for tsg in range(10)]

# Utility Functions ...
def display(game_board):
    print('\n   |   |\n'+' ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3]+'\n   |   |')
    print('-----------')
    print('\n   |   |\n'+' ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6]+'\n   |   |')
    print('-----------')
    print('\n   |   |\n'+' ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9]+'\n   |   |')

def BoardFull(game_board):
    if game_board.count(' ') <= 1:
        return True
    return False
    
def free_space(pos):
    return game_board[pos] == ' '

def help():
    print("\nThe individual cell-numbers are shown graphically: -------->>> \n")
    print('\n   |   |\n'+' ' + '1' + ' | ' + '2' + ' | ' + '3' +'\n   |   |')
    print('-----------')
    print('\n   |   |\n'+' ' + '4' + ' | ' + '5' + ' | ' + '6' +'\n   |   |')
    print('-----------')
    print('\n   |   |\n'+' ' + '7' + ' | ' + '8' + ' | ' + '9' +'\n   |   |')

def winner(game_board,h):
    return (game_board[1] == h and game_board[2] == h and game_board[3] == h) or (game_board[4] == h and game_board[5] == h and game_board[6] == h) or(game_board[7] == h and game_board[8] == h and game_board[9] == h) or(game_board[1] == h and game_board[4] == h and game_board[7] == h) or(game_board[2] == h and game_board[5] == h and game_board[8] == h) or(game_board[3] == h and game_board[6] == h and game_board[9] == h) or(game_board[1] == h and game_board[5] == h and game_board[9] == h) or(game_board[3] == h and game_board[5] == h and game_board[7] == h)

def user_Move():
    action = True
    while action:
        m = input('\nPlease type a cell-number to place your --> \'X\' [given cell numbers: (1-9)]: [type >> "405 " << for "help" to check the cell structure] : \t')
        try:
            m = int(m)
            if m == 405:
                help()
            if m > 0 and m < 10:
                if free_space(m):
                    game_board[m]= 'X'
                    action = False
                else:
                    print('\nSorry, this space is already occupied!')
            else:
                print('\nPlease type a cell-number within the given range (1-9]!')
        except:
            print('\nPlease type a cell-number!')

def comp_Move():
    possible = [x for x, letter in enumerate(game_board) if letter == ' ' and x != 0]
    m = 0

    for let in ['O', 'X']:
        for i in possible:
            board = game_board[:]
            board[i] = let
            if winner(board, let):
                m = i
                return m

    corners = []
    for i in possible:
        if i in [1,3,7,9]:
            corners.append(i)
            
    if len(corners) > 0:
        m = corners[random.randrange(0,len(corners))]
        return m

    if 5 in possible:
        m = 5
        return m

    edges = []
    for i in possible:
        if i in [2,4,6,8]:
            edges.append(i)
            
    if len(edges) > 0:
        m = edges[random.randrange(0,len(edges))]
        
    return m


# Main Function
def main():
    flag=0
    
    print('\n ----***---- !Welcome to the Tic Tac Toe game! ----***---- \n')
    help()
    print('\n--------------------------------------')
    print('--------------------------------------')
    print('\n\n------------ LET\'S PLAY --------------')
    print("\nCurrent Board :")
    display(game_board)

    while not(BoardFull(game_board)):
        if not(winner(game_board, 'O')):
            user_Move()
            print("You Entered : --------------->> (check below)")
            display(game_board)
        else:
            print('\nSorry, O\'s [computer] won this time!')
            break

        if not(winner(game_board, 'X')):
            m = comp_Move()
            if m == 0:
                print('\n!!It\'s a Tie Game!!')
                flag=1
            else:
                game_board[m]= 'O'
                print("\nPlease Wait! ...")
                time.sleep(2)
                print('\nComputer placed an \'O\' in position', m , '--------->> (check below)')
                display(game_board)
        else:
            print('\n[You] won this time!! Nice!')
            break

    if (BoardFull(game_board)and flag != 1):
        print('\n!!It\'s a Tie Game!!')


# Driver Code
p=0
while 1:
    if (p==0):
        game_board = [' ' for tsg in range(10)]
        main()
    
    p=1
    ts = input('\nWanna play again ?? (Y/N) \t')
    
    if (ts.lower == 'yes'  or  ts.lower() == 'y'):
        game_board = [' ' for tsg in range(10)]
        print('--------------------------------------')
        main()

    elif (ts.lower == 'no' or ts.lower() == 'n'):
        print("\n---**---       Thank you for Playing! ~ TSG405       ---**---")
        break
    else:
        print("Wrong Input, please enter [Y or N]")


@ CODED BY TSG405, 2020 
