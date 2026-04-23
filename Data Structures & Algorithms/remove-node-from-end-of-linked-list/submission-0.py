# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # get length of list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        if n == length:
            return head.next

        position = length - n
        cur = head
        tmp = None

        for i in range(position):
            tmp = cur
            cur = cur.next

        tmp.next = cur.next
        return head