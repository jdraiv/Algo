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
    print(result)

bouncer(["hello", 1, "", "test", 0,  True, False, None])
bouncer(["a", "b", "c"])