import random
import string
from random import randint

def key_generator():
    letters = "abcdefghijklmnopqrstuvwxyz"

    i = 0
    key = []
    for i in range(1,9):
        if i % 2 == 0:
            random_number = (randint(0,9))
            key.append(random_number)
        else:
            random_digit = random.choice(letters)
            random_digit = random_digit.capitalize()
            key.append(random_digit)
    return key

print(key_generator())
    
