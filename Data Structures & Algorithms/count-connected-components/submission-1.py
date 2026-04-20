class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list
        d = {}
        for a, b in edges:
            if a not in d:
                d[a] = []
            d[a].append(b)
            if b not in d:
                d[b] = []
            d[b].append(a)
        
        visited = set()

        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            if cur in d:
                for n in d[cur]:
                    dfs(n)
            return 
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
            