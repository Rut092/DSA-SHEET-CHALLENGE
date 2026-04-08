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
        if not head: return head 
        curr = head
        while(curr):
            temp = Node(curr.val)
            nxt = curr.next
            curr.next = temp
            temp.next = nxt
            curr = nxt

        curr = head
        while(curr):
            r_temp = curr.random
            curr = curr.next
            curr.random = r_temp.next if r_temp else None
            curr = curr.next

        head = head.next

        curr = head
        while(curr.next):
            curr.next = curr.next.next
            curr = curr.next
        curr = head

        return head