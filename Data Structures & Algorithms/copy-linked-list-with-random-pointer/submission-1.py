"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        copies = {}

        newList = newHead = Node(head.val)
        pointer = head

        while pointer:
            copies[pointer] = newList
            if pointer.next:
                newList.next = Node(pointer.next.val)
            pointer = pointer.next
            newList = newList.next

        newList = newHead
        pointer = head
        while pointer:
            if pointer.random:
                newList.random = copies[pointer.random]
            pointer = pointer.next
            newList = newList.next

        return newHead