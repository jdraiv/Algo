def longest(s):
    words = s.split()
    word_len = 0
    largest = ""

    for a in words:
        if len(a) > word_len:
            word_len = len(a)
            largest = a

    return "The largest word is: %s, Length: %s" % (largest,word_len)


test = "Hello my name is"
print(longest(test))