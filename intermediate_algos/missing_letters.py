#Find the missing letter in the passed letter range and return it.

#If all letters are present in the range, return undefined.

import string
def missing_l(s):
    alphabet = list(string.ascii_lowercase)
    result = ""
    
    c = alphabet.index(s[0])

    for l in range(0,len(s)):
        if s[l] != alphabet[c]:
            result += alphabet[c]
            c += 2
        else:
            c += 1
    if len(result) == 0:
        return "Undefined"
    else:
        return result

print(missing_l("abce"))
print(missing_l("abcdefghjklmno"))
print(missing_l("bcd"))