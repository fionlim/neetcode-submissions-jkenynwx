class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        for row in grid:
            print(row)

        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in visited:
                return 0
            
            if grid[x][y] == 1:
                visited.add((x, y))
                return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
            
            else:
                return 0


        for x in range(ROWS):
            for y in range(COLS):
                res = max(dfs(x, y), res)
        
        return res