

def prime(n):
    if n < 2:
        return False
    
    for a in range(2,n):
        if not n % a:
           return False
    return True 

    
    
def sum_primes(n):
    result = 0
    for a in range(0,n + 1):
        if prime(a) == True:
            result += a
    print(result)
    
sum_primes(10)
sum_primes(977)