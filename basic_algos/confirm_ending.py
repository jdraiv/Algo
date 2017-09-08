
#Check if a string (first argument, str) ends with the given target string (second argument, target)

def confirm_ending(string,target):
    string = string.lower()
    last_digit = string[len(string) - 1:]

    if last_digit == target.lower():
        return True
    else:
        return False

print(confirm_ending("Hello", "o"))
print(confirm_ending("Helly", "o"))