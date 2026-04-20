class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(x, y, visited, min_height):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in visited or heights[x][y] < min_height:
                return
            if heights[x][y] >= min_height:
                visited.add((x, y))
                min_height = heights[x][y]
                dfs(x + 1, y, visited, min_height)
                dfs(x - 1, y, visited, min_height)
                dfs(x, y + 1, visited,min_height)
                dfs(x, y - 1, visited, min_height)
        
        pacific_start = [(0, i) for i in range(COLS)] + [(i, 0) for i in range(1, ROWS)]
        atlantic_start = [(i, COLS - 1) for i in range(ROWS - 1)] + [(ROWS - 1, i) for i in range(0, COLS)]

        pac = set()
        atl = set()
        for x, y in pacific_start:
            dfs(x, y, pac, 0)
        for x, y in atlantic_start:
            dfs(x, y, atl, 0)

        return list(pac.intersection(atl))



        

        

        


        
                

            
            