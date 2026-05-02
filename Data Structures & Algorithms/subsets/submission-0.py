class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i, cur):
            if i >= len(nums):
                return
            cur.append(nums[i])
            res.append(cur.copy())
            dfs(i + 1, cur)

            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])
        res.append([])
        return res