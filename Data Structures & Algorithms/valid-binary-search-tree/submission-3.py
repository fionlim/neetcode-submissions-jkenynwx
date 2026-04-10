# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = []
        tracker = []
        queue.append(root)
        tracker.append((None, None)) # LL, UL
        while len(queue) > 0:
            queue_val = [node.val for node in queue]
            node = queue.pop(0)
            lower_limit, upper_limit = tracker.pop(0)
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and node.val >= upper_limit:
                return False
            if node.left:
                queue.append(node.left)
                tracker.append((lower_limit, node.val))
            if node.right:
                queue.append(node.right)
                tracker.append((node.val, upper_limit))
        return True