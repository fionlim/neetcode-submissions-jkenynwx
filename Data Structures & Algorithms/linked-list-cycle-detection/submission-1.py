# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # ideation
        # start tgt
        slow_ptr, fast_ptr = head, head.next
        # use a loop to make sure u have global state
        #               f                
        #             s                            
        # 0 1 2 3 4 5 6 7 8 9 10
        #             |     |
        #              -----
        while fast_ptr is not None and fast_ptr.next is not None:
            if fast_ptr == slow_ptr:
                return True
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return False
            

        # fion's working
        # if fast_pointer is None:
        #     return False
        # if slow_pointer.val == fast_pointer.val:
        #     return True
        # return self.hasCycle(head.next)