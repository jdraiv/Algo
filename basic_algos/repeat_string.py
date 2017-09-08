#Repeat a given string (first argument) num times (second argument).
#Return an empty string if num is not a positive number.

def repeat_string(string, num):
    result = ""
    if num > 0 :
        for a in range(0,num):
            result += string
        return result
    else:
        return result

print(repeat_string("abc", 3))
print(repeat_string("*", 2))