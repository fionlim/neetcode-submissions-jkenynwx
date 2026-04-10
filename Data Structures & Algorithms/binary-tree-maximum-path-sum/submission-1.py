# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = None
        def dfs(node):
            if node is None:
                return 0
            else:
                left_branch_sum = node.val + dfs(node.left)
                right_branch_sum = node.val + dfs(node.right)
                max_res = max(
                    node.val, 
                    node.val + dfs(node.left) + dfs(node.right),
                    left_branch_sum,
                    right_branch_sum
                )
                if self.max is None or max_res > self.max:
                    self.max = max_res
                return max(node.val, left_branch_sum, right_branch_sum)
        dfs(root)
        return self.max
