import random

score = 0
while True:
  
  print("\nEnter your range of guessing numbers:   If you want to play with default settings, then press: d   or   press: n [To exit from the game anytime, press t]:\n")
  user=input().lower()
  
  if user == 't':
      print('Game Over.  Thank you!')
      break
  
  if user=="d":
      num = random.randint(0,20)
      guess = input("\nGuess a number between {} to {}: ".format(0,20))  
  
  if user=="n":
      
      try:
          m=int(input("\nEnter your least range in numerics... eg. 10 , 20 , 45 , ..etc --->"))
      except:
          print("\nWrong Input! Follow instructions")
          continue
        
      try:
          n=int(input("Enter your max range in numerics... eg. 15 , 25 , 47 , ..etc --->"))
      except:
          print("\nWrong Input! Please follow instructions!")
          continue
      
      if n>=m:
          num = random.randint(m,n)
          guess = input("\nGuess a number between {} to {}: ".format(m,n))
      
      else:
          num = random.randint(n,m)
          guess = input("\nGuess a number between {} to {}: ".format(n,m))
 
  if guess == 't' or guess == 'T':
      print('Game Over.  Thank you!')
      break
  
  try:
      guess_num = int(guess)
  except:
      print("Wrong Input! Try using a numeral, next time! Let's start from the beginning!")
      continue
  
  if guess_num is num:
      print('CONGRATS!!! , You guessed it correctly!')
      score += 100
      print('Your new score:', score)
  
  else:
      print('SORRY!!!, Your guess did not match!')
      print('The number was:', num)


@ CODED BY TSG405, 2020
