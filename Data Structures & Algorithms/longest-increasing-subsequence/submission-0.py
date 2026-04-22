class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = {}
        global res
        res = 0

        def dfs(i):
            global res
            if i == len(nums) - 1:
                lis[i] = 1
            temp = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    if j not in lis:
                        dfs(j)
                    temp = max(temp, lis[j])
            lis[i] = temp + 1
            res = max(res, lis[i])
        
        for i in range(len(nums)):
            dfs(i)
        return res