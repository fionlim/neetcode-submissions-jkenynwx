class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        d = {}
        # create adjacency list
        for a, b in edges:
            if a not in d:
                d[a] = []
            if b not in d:
                d[b] = []
            d[a].append(b)
            d[b].append(a)


        visited = set()
        path = set()

        def dfs(cur, prev): # find cycle
            if cur in path:
                return True
            if cur not in d: # no edges connected 
                return False 
            visited.add(cur)
            path.add(cur)
            for n in d[cur]:
                if n == prev:
                    continue
                if dfs(n, cur):
                    return True 
            path.remove(cur)
            return False

        num_sets = 0
        for i in range(n):
            if i not in visited:
                num_sets += 1
            if dfs(i, None):
                return False
        
        return num_sets <= 1
