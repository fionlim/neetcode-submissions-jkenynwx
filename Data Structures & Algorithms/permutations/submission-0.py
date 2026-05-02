class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            cur.append(nums[i])
            if len(cur) == len(nums):
                res.append(cur.copy())
            for j in range(len(nums)):
                if nums[j] not in cur:
                    dfs(j, cur)
            cur.remove(nums[i])
        
        for i in range(len(nums)):
            dfs(i, [])
        
        return res