import random

# Word-List
def select_word():
    words = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","blitz","blizzard","boggle","bookworm",
              "boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri",
              "dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness",
              "flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess",
              "haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu",
              "jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx",
              "lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize",
              "oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum",
              "razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied",
              "subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","tsg","twelfth","twelfths","unknown","unworthy","unzip",
              "uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy",
              "witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]
    word = words[random.randint(0, len(words)-1)]
    return word

# DISPLAY
def get_blank_word(word):
    blank_word = word[0]
    for tsg in range(1, len(word)):
            blank_word += '_'
    return blank_word

# Main Function
def word_hangman(word, so_far, letter, try_left):
    bad_try = True
    for i in range(0, len(word)):
            if word[i] == letter:
                    so_far = so_far[:i]+letter+so_far[i+1:]
                    bad_try = False
    if bad_try is True:
            try_left -= 1
            print('Wrong Guess!! Tries Left: ', try_left)
    print('\nSo far you got :-->> ', so_far)
    if word == so_far:
            print('\nYAY!!! You Won the GAME!!\n')
    elif try_left == 0:
            print('\nOops!!! You Lost :(\n')
    else:
     print("\nLETTERS LEFT --->",so_far.count('_'))
     next_letter = input ('Enter your next guess(letter) :--- ')
     word_hangman(word, so_far, next_letter, try_left)


# Driver Function....
decision ='1'
while (decision == '1'):
    print("\n!*! WELCOME To The Hangman-Game !*!\n")
    word = select_word()
    clue_word = get_blank_word(word)
    word_hangman(word, clue_word, word[0], 5)
    decision=input("\nWant to play again? Type 1 for Yes, Type 0 for No ---> \n")
    if decision=='0':
        print("\nThank you for playing! Bye!\n")
        
        
@ CODED BY TSG405, 2020 
