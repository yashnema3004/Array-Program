class Solution:
    def getMinMax(self, arr):
        arr.sort()
        n = len(arr)
        minimum = arr[0]
        maximum = arr[n-1]
        
        return [minimum , maximum]
    