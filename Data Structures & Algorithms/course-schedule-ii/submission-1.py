class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}
        complete = {i: False for i in range(numCourses)}
        res = []
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        def dfs(crs, path):
            if complete[crs]: # crs completed
                return True
            if crs in path:
                return False
            if courses[crs] == []: # prereq found
                res.append(crs)
                complete[crs] = True
                return True
            path.add(crs)
            for pre in courses[crs]:
                if not dfs(pre, path):
                    return False
            res.append(crs)
            complete[crs] = True
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        return res