class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = [] # global 

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy()) # cur will be modified down the recursion
                return 
            if i >= len(nums) or total > target: # no more candidates (nums) or total exceed target
                return 

            # 1st decision to include candidate i
            cur.append(nums[i]) # update cur
            dfs(i, cur, total + nums[i])

            # 2nd decision: don't include candidate i, go to next candidate
            # pointer i is shifted but cur combi and total stays the same 
            cur.pop() # cur returns to prev 
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res
            
            

            
            
        