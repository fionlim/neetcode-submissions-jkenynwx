class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # cache

        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy: 
                buy_res = dfs(i + 1, False) - prices[i]
                cooldown_res = dfs(i + 1, True) 
                dp[(i, buy)] = max(buy_res, cooldown_res)
            else:
                sell_res = dfs(i + 2, True) + prices[i] # buy day after
                cooldown_res = dfs(i + 1, False) # cooldown 
                dp[(i, buy)] = max(sell_res, cooldown_res)
            return dp[(i, buy)]
        return dfs(0, True)


