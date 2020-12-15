import random

s1=0
s2=0

# LOGICAL FUNCTION
def winner(p1, p2):
   
   global s1
   global s2
   
   if (p1 == p2):
       s1+=1
       s2+=1
       return ("It's a tie!")
   
   elif (p1 == 'r'):
       if (p2 == 's'):
           s1+=1
           return ("First Player wins!")
       else:
           s2+=1
           return ("Computer wins!")
   
   elif (p1 == 's'):
       if (p2 == 'p'):
           s1+=1
           return ("First Player wins!")
       else:
           s2+=1
           return ("Computer wins!")
           
   elif (p1 == 'p'):
       if (p2 == 'r'):
           s1+=1
           return ("First Player wins!")
       else:
           s2+=1
           return ("Computer wins!")
   
   else:
       return ("Invalid Input!")

print(" --- ** --- !WELCOME TO THE R.P.S GAME! [vs COMPUTER] --- ** --- ")
try:
    c=int(input("\nHow many rounds will you like to play? Enter that number:"))
except:
    print("INVALID INPUT! Try again, next time!")
    exit()

if c<=0:
    print("Negative number not allowed! Redirecting to 1 round only!")
    c=1
    
# DRIVER CODE...
while(c>0):
    print("\nRounds left -->",c)
    player1 = input("\nFirst player: rock [enter 'r'], paper [enter 'p'] or scissors [enter 's']: ").lower()
    comp = random.choice(['r','p','s'])
    print("Computer Entered: ",comp)
    print(winner(player1, comp))
    c-=1

# RESULTS
if s1>s2:
    print("\nUltimate Winner ---> First Player")
elif s1<s2:
    print("\nUltimate Winner ---> Computer")
else:
    print("\nTie GAME!")
    
    
@ CODED BY TSG405, 2020       
