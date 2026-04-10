# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curr_queue = []
        next_queue = []
        curr_queue.append(root)
        res = []
        sublist = []
        while curr_queue:
            node = curr_queue.pop(0)
            if node:
                sublist.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            # check if current queue is finished
            if len(curr_queue) == 0:
                # add to result
                if sublist:
                    res.append(sublist)
                # reset sublist for next level 
                sublist = []
                # next queue becomes curr queue to iterate through
                curr_queue = next_queue
                # reset next queue for next level
                next_queue = []
        return res
