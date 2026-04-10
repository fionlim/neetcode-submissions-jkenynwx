# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder traversal:
        process node then node.left then node.right
        inorder traversal:
        process left subtree then root then right subtree
        using preorder, we know the root node
        """
        hashmap = {val: ind for ind, val in enumerate(inorder)}
        self.idx = 0 # start with root in preorder
        def dfs(left, right): # return TreeNode or None
            if left > right:
                return None
            val = preorder[self.idx]
            self.idx += 1
            inorder_id = hashmap[val]
            
            print('left: ' + str(left))
            print('right: ' + str(right))
            left_node = dfs(left, inorder_id - 1)
            right_node = dfs(inorder_id + 1, right)
            return TreeNode(val, left_node, right_node)
        return dfs(0, len(inorder) - 1)


            
            
    

