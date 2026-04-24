class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {} # adjacency list of courses mapped to prereqs
        for i in range(numCourses):
            d[i] = []

        for crs, prq in prerequisites:
            d[crs].append(prq)

        def dfs(crs, visited):
            if crs in visited: # cycle detected
                return False

            if d[crs] == []:
                return True # can be completed because no prq

            visited.add(crs)
            for prq in d[crs]:
                if dfs(prq, visited):
                    continue
                else:
                    return False
            visited.remove(crs) # so that other crs with the same prq can visit again
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True
            