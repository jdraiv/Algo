#Return true if the string in the first element
#of the array contains all of the letters of the string in the second element of the array.

def mutations(arr):
    result = True
    for letter in arr[1]:
        if letter.lower() not in arr[0].lower():
            result = False
    return result

print(mutations(["hEllo","Hello"]))
print(mutations(["Alien","line"]))