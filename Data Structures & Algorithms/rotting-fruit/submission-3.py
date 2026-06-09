class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        d = {}  # dictionary to track min time to turn fruit rotten
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    d[(r, c)] = -1
        
        def bfs(r, c, curr):
            # bfs starting from rotten fruit in grid
            queue = []
            queue.append((r, c, 0))

            while queue:
                x, y, t = queue.pop(0)
                if d[(x, y)] == -1:
                    d[(x, y)] = t
                else:
                    d[(x, y)] = min(d[(x, y)], t)
                curr.add((x, y))
                directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for dx, dy in directions:
                    if 0 <= dx < ROWS and 0 <= dy < COLS and grid[dx][dy] == 1 and (dx, dy) not in curr:
                        queue.append((dx, dy, t + 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    bfs(r, c, set())
        
        if -1 in d.values(): # check if any fruits cannot be reached
            return -1

        if d.values():
            return max(d.values())

        return 0


