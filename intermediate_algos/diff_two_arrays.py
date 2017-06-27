#Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. In other words, return the symmetric difference of the two arrays.

def search_arr(obj, arr, container):
	if obj not in arr:
		container.append(obj)

def diff_array(arr1,arr2):
    result = []
    
    for obj_one, obj_two in zip(arr1,arr2):
    	search_arr(obj_one, arr2, result)
    	search_arr(obj_two,arr1,result)

    print(result)
    
    
diff_array(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])
diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5])