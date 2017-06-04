
#Check if a string (first argument, str) ends with the given target string (second argument, target)

def confirm_ending(str,target):
    last_digit = str[len(str) - 1:]

    if last_digit == target:
        print(True)
    else:
        print(False)


confirm_ending("Helly", "o")