class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l < r:
            if nums[l] < nums[r]:
                res = nums[l]
                return res
            m = (l + r) // 2
            if nums[m] >= nums[l]: # search right
                l = m + 1
            else: # search left 
                r = m
        return nums[r]