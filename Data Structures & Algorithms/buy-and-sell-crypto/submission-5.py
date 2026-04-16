class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        best_buy = [10e99,] * len(prices)
        best_buy[0] = prices[0]
        max_profit = prices[1] - best_buy[0]
        for i in range(1, len(prices) - 1):
            best_buy[i] = min(best_buy[i-1], prices[i])
            print("best buy:", best_buy)
            max_profit = max(max_profit, prices[i+1] - best_buy[i])

        return max(max_profit, 0)

        


            