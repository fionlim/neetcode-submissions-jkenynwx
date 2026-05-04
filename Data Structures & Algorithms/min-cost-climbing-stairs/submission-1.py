class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            res[i] = min(res[i - 1] + cost[i - 1], res[i - 2] + cost[i - 2])
        return res[-1]
