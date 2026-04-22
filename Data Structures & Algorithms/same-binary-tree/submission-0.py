# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global res
        res = True
        def dfs(p, q):
            global res
            if not p and not q:
                return
            if (p and q and p.val != q.val) \
            or (not p and q)\
            or (p and not q):
                res = False
                return
            else:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
        
        dfs(p, q)
        return res