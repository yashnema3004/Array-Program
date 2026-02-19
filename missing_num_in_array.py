class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        nums.sort()
        for i in range(0,n):
            if nums[i] == k:
                k+=1
        else:
            return k
