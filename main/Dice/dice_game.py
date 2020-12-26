import random

# Pattern Function..
def diceFace(num):
    print("\n=========")
    if num == 1:
        print("|     " + "  |"+"\n|   " + "0" + "   |"+"    * 1(ONE) *"+"\n|     " + "  |")
        
    if num == 2:  
        print("|     " + "  |"+"\n|  " + "0 0" + "  |"+"    * 2(TWO) *"+"\n|     " + "  |")

    if num == 3:     
        print("| 0   " + "  |"+"\n|   " + "0" + "   |""    * 3(THREE) *"+"\n|     " + "0 |")

    if num == 4:       
        print("| 0   " + "0 |"+"\n|       |"+"    * 4(FOUR) *"+"\n| 0   " + "0 |")
       
    if num == 5:      
        print("| 0   " + "0 |"+"\n|   " + "0" + "   |"+"    * 5(FIVE) *""\n| 0   " + "0 |")
       
    if num == 6:   
        print("| 0   " + "0 |"+"\n| 0   " + "0 |"+"    * 6(SIX) *""\n| 0   " + "0 |")

    print("=========\n")


# Driver Function..
def tsg():
    
    diceFaceNum = random.randint(1, 6)
    
    if diceFaceNum == 1:
        diceFace(1)
    elif diceFaceNum == 2:
        diceFace(2)
    elif diceFaceNum == 3:
        diceFace(3)
    elif diceFaceNum == 4:
        diceFace(4)
    elif diceFaceNum == 5:
        diceFace(5)
    elif diceFaceNum == 6:
        diceFace(6)
        
    print("Would you like to roll, once again ?")
    
    s = input("Enter y for yes and n for a no\n").lower()
    if s=='y' or s=='yes':
        tsg()
    elif s=='n' or s=='no':
        print("\nOkay no problem! Thank You!")
        print("~ TSG")


print("\n -----***----- WELCOME TO THE DICE-ROLLING GAME -----***----- \n")
tsg()


@ CODED BY TSG405, 2020
