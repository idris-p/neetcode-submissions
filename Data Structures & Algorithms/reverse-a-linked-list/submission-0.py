# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        l, r = head, head.next

        head.next = None
        while r:
            temp = r
            r = r.next
            temp.next = l
            l = temp

        return l
            