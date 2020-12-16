import random

digits = '123456789'
secret = ''.join(random.sample(digits,4))

print(" ----**---- Bulls & Cows ----**---- ")
print("\nGuess the Number.It contains 4 unique digits [repetition not allowed]!!\n ")

remaining_try = 10

# LOGICAL FUNCTION
def get_bulls_cows(number, user_guess):
   
   bulls_cows = [0,0] 
   for i in range(len(number)):
       if user_guess[i] == number[i]:
           bulls_cows[0] += 1
       elif user_guess[i] in number:
           bulls_cows[1] += 1
   
   return (bulls_cows)

# DRIVER CODE...
while remaining_try > 0:

   # Validating 4-Unique Digits in the Guess...
   while True:     
      player_guess = input("\nEnter your guess.. [Please enter a 4-digit non-repetitive numeral]: ").strip()
      
      if (len(player_guess) == 4 and all(char in digits for char in player_guess) and len(set(player_guess)) == 4):
          break
      print(" <<<<< PROBLEM! Please enter 4 Unique digits! >>>>> ")
   
   # Logic
   if player_guess == secret:
       print("\nWOW!! you guessed it right! \nYOU WIN!!")
       break
   
   else:
       bulls_cows = get_bulls_cows(secret,player_guess)
      
       print("Bulls: --> ",bulls_cows[0])
       print("Cows: --> ",bulls_cows[1])
       
       remaining_try -= 1
       print("\nTries Left ------> ",remaining_try)
       
       if remaining_try < 1:
           print("Sorry! You lost the game! Better Luck Next Time!! :(")
           break
           
           
@ CODED BY TSG405, 2020              
