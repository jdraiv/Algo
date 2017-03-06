

def vowels(string):
    vowels = ["a","e","i","o","u"]
    result = 0
    for i in string:
        if i in vowels:
            result = result + 1
    return result

print(vowels("test"))