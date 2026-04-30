# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # get diameter for each node
        # but return max height in recursive call
        global res
        res = 0

        def dfs(root):
            global res
            if root is None:
                return 0
            l, r = 0, 0
            if root.left:
                l = 1 + dfs(root.left)
            if root.right:
                r = 1 + dfs(root.right)
            
            res = max(l + r, res)
            return max(l, r)
        
        dfs(root)
        return res

