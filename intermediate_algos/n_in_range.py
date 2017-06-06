#We'll pass you an array of two numbers. Return the sum of those two numbers and all numbers between them.

def range_sum(arr):
    result = 0
    
    for n in range(min(arr),max(arr) + 1):
        result += n
    print(result)
        
        
range_sum([1,4])
range_sum([10,5])
range_sum([5,10])