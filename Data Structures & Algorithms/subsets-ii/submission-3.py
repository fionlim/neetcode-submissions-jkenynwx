class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def dfs(i, cur):

            if i >= len(nums):
                return

            cur.append(nums[i])
            res.append(cur.copy())

            dfs(i + 1, cur)

            while i + 1 <= len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])
        res.append([])

        return res

            

            