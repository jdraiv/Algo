#Return the lowest index at which a value (second argument) should be inserted into an array (first argument)
#once it has been sorted. The returned value should be a number.

def where(arr,n):
    arr = sorted(arr)
    c = 0
    for a in arr:
        if n > a:
            c += 1
        else:
            print(c)
            break
    
where([10,30,20,60,50],40)
where([10, 20, 30, 40, 50], 30)
where([5, 3, 20, 3], 5)