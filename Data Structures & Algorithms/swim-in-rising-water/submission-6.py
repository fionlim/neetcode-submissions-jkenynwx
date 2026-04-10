class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        for row in grid:
            print(row)
        processed = dict()
        queue = []
        start = (0,0)
        queue.append(start)
        processed[start] = grid[0][0]
        while len(queue) > 0:
            node = queue.pop(0)
            x, y = node
            # enqueue neighbours
            x1, x2, y1, y2 = x + 1, x - 1, y + 1, y - 1
            neighbours = [(x, y1), (x, y2), (x1, y), (x2, y)]
            for p, q in neighbours:
                # print(processed)
                if p < 0 or p >= len(grid) or q < 0 or q >= len(grid):
                    continue
                if (p, q) not in processed:
                    queue.append((p, q))
                    processed[(p, q)] = max(grid[p][q], processed[node])
                elif grid[p][q] < grid[x][y]:
                    queue.append((p, q))
                    processed[(p, q)] = min(processed[(p, q)], processed[node])
                elif grid[p][q] > grid[x][y]:
                    temp = max(processed[node], grid[p][q])
                    if temp < processed[(p, q)]:
                        queue.append((p, q))
                    processed[(p, q)] = min(temp, processed[(p, q)])
                else:
                    continue
        n = len(grid)
        return processed[(n-1, n-1)]

            
        