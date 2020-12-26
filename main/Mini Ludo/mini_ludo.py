import random

board=[]
level=3
Player_Pos=[1,1]
Dragon_Pos=[]
player=["A","B"]
gameEnd=False

# Utility Functions..
def create(lvl):
    global board,levelplayerPos,dragonPos
    board=[]
    Dragon_Pos=[]
    Player_Pos=[1,1]
    freePos=set()
    level=lvl
    
    for i in range(49):
        board.append({'B_type':""})
        if(i not in (0,48)):
            freePos.add(i+1)
            
    board[0]['B_type']="START"
    board[48]['B_type']="END"
    
    for ii in range(10):
        elems=random.sample(freePos,2)
        freePos.remove(elems[0])
        freePos.remove(elems[1])
        board[elems[0]-1]['B_type']="GOTO"
        board[elems[0]-1]['goto_val']=elems[1]


def draw():
    print("\n")
    for i in range(8):
        print(('+'+'-'*7)*7+'+')
        if i!=7:
            for line in range(3):
                for col in range(7):
                    n=7-i
                    pos=0
                    if(n%2==1):
                        pos=7*n-6+col
                    else:
                        pos=7*n-col
                    if line==1:
                        print(('|'+str(pos).center(7)),end='')
                    elif line==0:
                        posTitle=board[pos-1]['B_type']
                        if posTitle=="GOTO":
                            gotoPosNum=str(board[pos-1]["goto_val"])
                            posTitle+=' '+gotoPosNum
                        print(('|'+posTitle.center(7)),end='')
                    else:
                        players=''
                        if(Player_Pos[0]==pos):
                            players+="*A*"
                        if(Player_Pos[1]==pos):
                            players+="*B*"
                        print(('|'+players.center(7)),end='')
                print('|')
    input("\n\nPRESS enter to proceed...\n")
                        
def result(pos):
    if pos>49:
        return (49)
    if(board[pos-1]["B_type"]=='GOTO'):
        return result(board[pos-1]["goto_val"])
    else:
        return (pos)
    
def Possible_move(pos,disp):
    return 1<=disp+pos

def Input():
    if(not gameEnd):
        tsg=input("\nYou can move Forward [PRESS \"F\"] or Backward [PRESS \"B\"]  by this dice value. Enter \"end\" to end this game. your input:\t").lower()
        if tsg not in ('f','b','end'):
            print("Invalid input!!")
            return Input()
        return tsg
    
def moveP(pid,disp):
    global Player_Pos
    if(not gameEnd):
        Player_Pos[pid]=Player_Pos[pid]+disp
        draw()
    
        if(Player_Pos[pid]!=result(Player_Pos[pid])):
            Player_Pos[pid]=result(Player_Pos[pid])
            draw()
            
        if Player_Pos[pid]>=49:
            Player_Pos[pid]=49
            playerWins(pid)
    
def playerWins(pid):
    global level, gameEnd
    print('Player'+player[pid]+" wins this level!")
    gameEnd=True
  
  
# Driver code..
def main():
    create(level)
    print("\n--***-- WELCOME TO THE GAME --> MINI-LUDO --***--")
    print("\n\n Initialising Game Board ... ")
    current=0
    draw()
    while(not gameEnd):
        
        DICE=random.randrange(1,7)
        print("Player"+player[current]+"'s turn.")
        print("Rolling the dice...")
        print("Value on the dice is:",DICE)
        while(True):
            tsg=Input()
            if tsg=='end':
                print("Ending game...\n~ Thank You!")
                return
            if tsg=='b':
                disp=DICE*-1
            elif tsg=='f':
                disp=DICE
            if Possible_move(Player_Pos[current],disp):
                moveP(current,disp)
                break
            else:
                print("Move not possible! Please Try Again!")
        if (current==0):
            current=1
        else:
            current=0
                
main()


@ CODED BY TSG405, 2020
