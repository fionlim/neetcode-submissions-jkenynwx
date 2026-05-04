class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 > 0:
            return False

        target = sum(nums) // 2

        def dfs(i, cur):
            if sum(cur) == target:
                return True
            if sum(cur) > target or i >= len(nums):
                return False

            cur.append(nums[i])
            if dfs(i + 1, cur):
                return True

            cur.pop()
            return dfs(i + 1, cur)

        return dfs(0, [])