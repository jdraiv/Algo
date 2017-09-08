#Return the remaining elements of an array after chopping off n elements from the head.

def slasher(arr, chopp_n):
    return arr[chopp_n:]


print(slasher([1,2,3,],2))
print(slasher([1,2,3],0))


