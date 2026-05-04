# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverseList = slow.next
        slow.next = None

        l, r = None, reverseList
        while r:
            temp = r.next
            r.next = l
            l = r
            r = temp

        reverseList = l
        normalList = head
        
        while reverseList:
            pointer1 = normalList.next
            pointer2 = reverseList.next
            head.next = reverseList
            head = head.next
            normalList = pointer1
            reverseList = pointer2
            head.next = normalList
            head = head.next
