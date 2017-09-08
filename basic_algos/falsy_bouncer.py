#Remove all falsy values from an array.

def bouncer(arr):
    result = []
    for a in arr:
        if type(a) is str:
            if len(a) > 0:
                result.append(a)
        elif type(a) is bool:
            if a != False:
                result.append(a)    
        elif type(a) is int:
            if a != 0:
                result.append(a)
    return result

print(bouncer(["hello", 1, "", "test", 0,  True, False, None]))
print(bouncer(["a", "b", "c", "", False]))