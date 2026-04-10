# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Solution w two queues
        """res = []
        q = []
        next_q = []
        level = []
        q.append(root)
        while q:
            node = q.pop(0)
            if node:
                level.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
                
            if len(q) == 0:
                res.append(level)
                level = []
                q = next_q
                next_q = []
            
        print(res)
        final = []
        for level in res:
            if level:
                final.append(level.pop())
        return final"""

        # Solution using only 1 queue and queue length to keep track of levels

        res = []
        q = []
        q.append(root)
        while q:
            qlen = len(q)
            rightmost = None
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    rightmost = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost)
        return res
                    


            
