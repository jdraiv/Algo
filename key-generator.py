import random
import string


from random import randint

def key_generator():
    letters = "abcdefghijklmnopqrstuvwxyz"

    #digitOne = random.choice(letters)
    #digitOne = digitOne.capitalize()
    #digitTwo = (randint(0,9))
    i = 0
    key = []
    for i in range(1,9):
        if i % 2 == 0:
            randomNumber = (randint(0,9))
            key.append(randomNumber)
        else:
            randomDigit = random.choice(letters)
            randomDigit = randomDigit.capitalize()
            key.append(randomDigit)
    return key

print(key_generator())
    
