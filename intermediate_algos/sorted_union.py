def union(array):
    result = []
    for arr in array:
        for a in arr:
            if a not in result:
                result.append(a)
            elif isinstance(a, list):
                print(a)
    print(result)
        
union([[1,3,2],[5,2,1,4],[2,1,[5]]])