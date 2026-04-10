# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr_val = root.val
        lower_val = min(p.val, q.val)
        higher_val = max(p.val, q.val)
        if lower_val <= curr_val and higher_val >= curr_val:
            return root
        elif higher_val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)