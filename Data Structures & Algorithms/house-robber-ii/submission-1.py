class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return max(nums)

        def dp(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return max(rob1, rob2)

        return max(dp(nums[0:-1]), dp(nums[1:]))
            
