# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # start of 2nd half of linked list
        second = slow.next
        slow.next = None # split the 1st and 2nd half of list
        
        # reverse the 2nd linked list
        prev = None 
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge linked lists
        first = head
        second = prev
        counter = 0
        while second: # because 2nd is shorter
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = second.next
            second = tmp2
     



            


        
        



        
    









        

            


        