# Bulls & Cows

## Logic

This is a popular 'number' guessing game [4-digit number], previously used to crack codes! In this game, the user/player guesses the secret number.
So, if the user/player guesses the number correctly, he/she wins.
But if they didn’t guess the exact number, then the number of 'bulls' and 'cows' will be calculated alongside, as hints. 

Let’s say the number is: `5620`

And user's/player's guess is: `9826`

So, if he/she guesses any positioned digit currently, the person gets a 'bull'. For this guess, the user/player didn’t match the first, second or the last digit. 
However, he/she guessed the third digit correctly, with it's position!! Hence, here the number of bulls will be '1'.

On the other hand, if one or more digits of the secret number exists in the guess (irrespective of it's correct position), the player/user gets a cow!

Summarizing, if the user/player matched the digit with it's original position, a bull is counted!
Whereas, if the guess has the digit in a different place of the original/secret number, a cow is counted! 

In the above problem/guess, there is a '6' in the 4th position. The '6' exists in the secret number too, but in a different location! -- That's why the user/player gets 1 cow. 

Hence, in this round of guessing, the score will be: 

* Bulls: 1
* Cows: 1
 

Another example --->

* Secret number: 5079 
* user/player's guess: 9035

Answer:  1 bull and 2 cows. (The bull is "0", the cows are "5" and "9".)


## Objective

* `Within the stipulated amount of guessing rounds/re-tries, try to get 4 'Bulls', to match your guess with the secret number.`

## Constraints

* `The user/player has to input a four-digit numeral in every guess round. Eg: 1234, 4567, 2789.`
* `The user/player has to guess the actual number, within a stipulated amount of re-tries/guesses [i.e -> 10, in this game], to WIN!`


### ALL THE BEST!
##### @ CODED BY TSG405, 2020

tags: `python`  `python3`  `problem-solving`  `programming`  `coding-challenge`  `interview`  `learn-python`  `python-tutorial`  `programming-exercises`  `programming-challenges`  `programming-fundamentals`  `programming-contest`  `python-coding-challenges`  `python-problem-solving`
