

def find_word(text,string):
    textLen = len(text)
    stringLen = len(string)

    number = text.find(string)
    if number > 0:
        print('Word in text')
        number = number + stringLen -1
    return number



str1 = "this is string example....wow!!!"
str2 = "exam"

print(find_word(str1,str2))

