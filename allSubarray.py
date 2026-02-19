class Solution:
    def getSubArrays(self, arr):
        result = []
        
        for start in range(len(arr)):
            for end in range(start, len(arr)):
                result.append(arr[start:end+1])
                
        return result
