class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0 = cnt1 = cnt2 = 0
        n = len(nums)

    
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        i = 0

        while cnt0 > 0:
            nums[i] = 0
            i += 1
            cnt0 -= 1

        while cnt1 > 0:
            nums[i] = 1
            i += 1
            cnt1 -= 1

        while cnt2 > 0:
            nums[i] = 2
            i += 1
            cnt2 -= 1
