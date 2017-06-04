import random
from random import randint


def game():
    #Main Variables
    lives = 4
    play = True
    words = ["SOCCER","CHICKEN"]

    #Get a random word
    word = random.choice(words)
    #Get word length
    wordLength = len(word)
    #Send hint
    print("Hint: The word is %s character long" % (wordLength))

    correctLetters = ""
    incorrectLetters = []

    while play:
        if lives >= 1:
            print("Correct letters: %s" % correctLetters)
            print("Incorrect letters: %s" % incorrectLetters)

            guess = input("Guess a letter: ")
            guess = guess.capitalize()

            guessLen = len(guess)

            if guessLen <=1 and guess in word:
                correctLetters = correctLetters + guess
                print("Letter in word")

            elif guess not in word and guessLen <= 1:
                incorrectLetters.append(guess)
                lives = lives - 1
                print("Letter not in word")

            elif guessLen >= 1 and guess != word:
                print("Please only enter a letter or the complete word")

        elif correctLetters == word:
            print("You won!")
            play = False
            
        else:
            print("Game over")
            play = False


#Run game
game()


    
