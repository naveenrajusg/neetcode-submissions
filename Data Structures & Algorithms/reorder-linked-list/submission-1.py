# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # While fast reaches last, the slow will be pointing to end of first half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = None
        slow.next = None
        #reverse the second list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #reorder logic
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1






