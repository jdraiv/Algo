

def fibo(num):
    result = [0,1]
    total = 0
    
    for a in range (num):
        if a == num - 1:
            #print(result[-1] + result[-2])
            pass
        else:
            result.append(result[-1] + result[-2])
    return result

print(fibo(4))
