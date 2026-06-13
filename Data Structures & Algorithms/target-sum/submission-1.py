class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, total):
            res = 0
            if i == len(nums) - 1 and (total + nums[i] == target):
                res += 1
            if i == len(nums) - 1 and (total - nums[i] == target):
                res += 1
            if i < len(nums) - 1:
                res = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return res

        return dfs(0, 0)