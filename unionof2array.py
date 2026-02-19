def unionof2array(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i +=1
        else:
            if not res or res[-1] != arr2[j]:
                res.append(arr2[j])
            j +=1 
    
    
    while i < len(arr1):
        if not res or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1


    while j < len(arr2):
        if not res or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1
    
    return res
