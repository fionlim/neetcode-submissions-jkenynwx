class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}

        if len(prerequisites) == 0:
            return True

        for a, b in prerequisites: # map each prereq to courses it fulfills
            if b not in d:
                d[b] = []
            d[b].append(a)

        visited = set() # global visited to avoid re-processing nodes
        path = set()    # track nodes in current recursion for cycle detection

        def dfs(cur):
            if cur in path: # cycle detected
                return True
            if cur in visited:
                return False
            
            visited.add(cur)
            path.add(cur)
            if cur in d:
                for n in d[cur]:
                    if dfs(n):
                        return True
            path.remove(cur)
            return False
        
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        return True