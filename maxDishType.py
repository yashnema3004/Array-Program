def maxDishtype(A,N):
    
    dish_type = set(A)
    max_count = 0
    best_type = float('inf')
    
    for t in dish_type:
        i = 0
        count = 0
        while i < N:
            if A[i] == t:
                count +=1
                i +=2
            else:
                i+=1
            
        if count > max_count or (count == max_count and t < best_type):
            max_count = count
            best_type = t
        
    return best_type
                

R = [1,2,2,1,2,1,1,1,1]
s = 9

print(maxDishtype(R,s))
        
