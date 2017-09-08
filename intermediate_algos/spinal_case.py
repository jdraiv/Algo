import string

def spinal_case(s):
    alphabet_l = string.ascii_lowercase
    alphabet_u = string.ascii_uppercase

    result = ""
    letters = list(s)
    
    c = 0
    for a in letters:
        if c == 0:
            result += a.lower()
            c += 1
        elif a == " ":
            result += '-'
            
        elif a in alphabet_l:
            result += a
        
        elif a in alphabet_u:
            result += '-' + a.lower()
            
        else:
            result += '-'

    return result
    
        
        
print(spinal_case("This is spinal case"))
print(spinal_case("thisIsSpinalCase"))
print(spinal_case("AllThe-small Things"))