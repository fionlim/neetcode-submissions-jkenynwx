class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...] 
        # rob2: last house we robbed
        # rob1: house before that
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return max(rob1, rob2)
        

        # global highest
        # highest = 0

        # def dfs(cur, total):
        #     global highest
        #     if cur > len(nums) - 1:
        #         return

        #     total += nums[cur]
        #     highest = max(total, highest)

        #     for i in range(cur + 2, len(nums)):
        #         dfs(i, total)

        # for i in range(len(nums) // 2 + 1):
        #     dfs(i, 0)
        
        # return highest



