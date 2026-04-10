# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodesHelper(node, max_val):
            if node is None:
                return 0
            elif max_val is None or node.val >= max_val:
                return 1 + goodNodesHelper(node.left, node.val) + goodNodesHelper(node.right, node.val)
            else:
                return goodNodesHelper(node.left, max_val) + goodNodesHelper(node.right, max_val)
        return goodNodesHelper(root, None)




            
