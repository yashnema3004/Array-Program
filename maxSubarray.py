class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            total = max(nums[i], total + nums[i])
            maxSum = max(maxSum, total)
        
        return maxSum
