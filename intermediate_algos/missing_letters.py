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
        print("Undefined")
    else:
        print(result)

missing_l("abce")
missing_l("abcdefghjklmno")
missing_l("bcd")