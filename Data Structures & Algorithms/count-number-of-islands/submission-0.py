class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def dfs(x, y, cur):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in visited:
                return cur

            visited.add((x, y))
            if grid[x][y] == "1":
                cur.append((x, y))
                dfs(x + 1, y, cur)
                dfs(x - 1, y, cur)
                dfs(x, y + 1, cur)
                dfs(x, y - 1, cur)
            return cur

        for x in range(ROWS):
            for y in range(COLS):
                island_size = len(dfs(x, y, []))
                if island_size > 0:
                    res += 1
        
        return res




