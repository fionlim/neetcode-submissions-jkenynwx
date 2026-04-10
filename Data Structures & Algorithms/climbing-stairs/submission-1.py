class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        num_ways = 0
        for i in range(1, 3):
            num_ways += self.climbStairs(n - i)
        return num_ways