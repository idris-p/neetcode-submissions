# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next

        if length < 2:
            return None
        if length == n:
            return head.next

        pointer = head
        for i in range(length - n - 1):
            pointer = pointer.next

        temp = pointer.next
        pointer.next = temp.next

        return head