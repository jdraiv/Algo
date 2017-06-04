
def largest_of_four(arr):
    #Return an array consisting of the largest number from each provided sub-array. 
    result_arr = []

    for array in arr:
        largest_n = max(array)
        result_arr.append(largest_n)

    print(result_arr)

largest_of_four([ [1,2,3,4] , [1,2,8,9], [20,15,100,8], [29,30,10,5] ])
