def maxsubarray(a,k):
    maxSum = 0
    for i in range(a):
        if a[i] >= 0 :
            maxSum += a[i]
    if maxSum >= 0:
        return maxSum
    else:
        return max(a)
            

        
    
