class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        currArea = 0
        maxArea = 0
        while left < right:
            br = right - left
            hei = min(height[left] , height[right])
            currArea = br * hei

            maxArea = max(currArea , maxArea)

            if height[left] < height[right]:
                left +=1
            else:
                right  -=1

        return maxArea

        

            
        




        

        
