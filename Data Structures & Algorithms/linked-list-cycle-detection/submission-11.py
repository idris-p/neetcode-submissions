# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head

        while hare:
            tortoise = tortoise.next
            if hare.next:
                hare = hare.next.next
            else:
                return False

            if tortoise == hare:
                return True

        return False

