"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return 
        d = {} # store nodes already cloned
        def dfs(cur):

            if cur.val in d: # already cloned
                return d[cur.val]

            # if not cloned yet
            clone = Node(cur.val)
            d[cur.val] = clone

            for n in cur.neighbors:
                d[cur.val].neighbors.append(dfs(n)) 

            return d[cur.val]

        return dfs(node)


            