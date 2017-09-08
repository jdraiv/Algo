
def search_and_replace(string, before, after):
    string = string.replace(before, after)
    return string
    
print(search_and_replace("Let us go to the store", "store", "mall"))

print(search_and_replace("He is Sleeping on the couch", "Sleeping", "sitting"))
