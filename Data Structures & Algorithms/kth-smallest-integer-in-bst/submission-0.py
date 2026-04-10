# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            res = []
            if node.left:
                res = traverse(node.left) + res
            res.append(node.val)
            if node.right:
                res = res + traverse(node.right)
            return res
        res = traverse(root)
        return res[k - 1]
            


