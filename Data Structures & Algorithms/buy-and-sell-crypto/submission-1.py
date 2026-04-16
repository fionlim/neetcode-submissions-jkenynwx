class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy_idx in range(len(prices)):
            for sell_idx in range(buy_idx + 1, len(prices)):
                max_profit = max(max_profit, prices[sell_idx] - prices[buy_idx])
        return max_profit
        


            