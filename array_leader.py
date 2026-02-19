def arrayLeader( arr):
    
    maxEl = arr[-1]
    for i in range(len(arr)-1,0,-1):
        maxEl = max(maxEl , arr[i])
    
    return maxEl
