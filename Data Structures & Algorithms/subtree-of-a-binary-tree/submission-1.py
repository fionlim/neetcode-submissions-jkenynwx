# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2)\
            or (root1 and not root2)\
            or (root1.val != root2.val):
                return False
            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

        if sameTree(root, subRoot):
            return True
        
        l = False
        r = False
        if root.left:
            l = self.isSubtree(root.left, subRoot)
        if root.right:
            r = self.isSubtree(root.right, subRoot) 

        return l or r
        

