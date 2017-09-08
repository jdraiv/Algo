

def find_word(text,string):
    text_len = len(text)
    string_len = len(string)

    number = text.find(string)
    if number > 0:
        number = number + string_len -1
    return number



str1 = "this is string example....wow!!!"
str2 = "exam"

print(find_word(str1,str2))

