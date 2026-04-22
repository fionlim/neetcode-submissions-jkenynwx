class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache =[[0 for i in range(n)] for j in range(m)]

        def dp(x, y):
            if x == 0 or y == 0:
                cache[x][y] = 1
                return 1

            res = 0
            if cache[x][y] > 0:
                res = cache[x][y]
            else:
                res = dp(x, y-1) + dp(x - 1, y)
                cache[x][y] = res
            return res

        
        return dp(m-1, n-1)