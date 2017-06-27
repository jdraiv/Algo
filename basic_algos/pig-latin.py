
def pig_latin(string):
    firstLetter = string[0]
    string = string[1:] + firstLetter +"ay"
    return string

print(pig_latin("pig"))

