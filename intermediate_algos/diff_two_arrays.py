#Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. In other words, return the symmetric difference of the two arrays.

def diff_array(arr1,arr2):
    result = []
    
    for a in arr1:
        if a not in arr2:
            result.append(a)
            
    for a in arr2:
        if a not in arr1:
            result.append(a)
    print(result)
    
    
diff_array(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])

diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5])