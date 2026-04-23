class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        counter = 0
        for num in nums:
            if num != counter:
                return counter
            counter += 1
        return counter