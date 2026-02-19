class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  
        
        def rev(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        rev(0, d-1)
        rev(d, n-1)
        rev(0, n-1)
        
        return arr
