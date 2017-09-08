#You will be provided with an initial array (the first argument in the destroyer function),
# followed by one or more arguments.
# Remove all elements from the initial array that are of the same value as these arguments.

def destroyer(arr, find1, find2):
    result = []
    
    for a in arr:
        if a != find1 and a != find2:
            result.append(a)
    return result

print(destroyer([1,2,2,3,4,10,3,4,5], 1, 2))
