def cap(s):
    words = s.split()
    result = ""
    c = 1
    
    for a in words:
        if c == 1:
            c += 1
            result += a.capitalize()
        else:
            result += ' ' + a.capitalize()
    return result
        
test = "I am a little tea pot"
test2 = "How our bodies, born to heal, become so prone to die?"

print(cap(test))
print(cap(test2))