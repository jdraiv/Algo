
def palindrome(string):
    palindrome_verif = string[::-1]
    if palindrome_verif == string:
        return "String is palindrome"
    else:
        return "Not palindrome"

print(palindrome("racecar"))
print(palindrome("marram"))
print(palindrome("test"))