class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(x, y):
            # find all tiles that reach 0, starting from 0
            q = []
            q.append((x, y, 0))
            visit = set()
            
            while q:
                r, c, res = q.pop(0)
                
                if (r, c) in visit or grid[r][c] == -1:
                    continue
                
                visit.add((r, c))

                if grid[r][c] != 0 and grid[r][c] != -1:
                    grid[r][c] = min(grid[r][c], res)

                for dx, dy in directions:
                    r_new, c_new = r + dx, c + dy
                    if 0 <= r_new < ROWS and 0 <= c_new < COLS:
                        q.append((r_new, c_new, res + 1))
            
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0:
                    bfs(x, y)
        