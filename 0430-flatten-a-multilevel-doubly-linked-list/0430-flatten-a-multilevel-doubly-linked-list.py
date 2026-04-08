"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return 
        stack = [head]
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while(stack):
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            while(curr):
                prev = curr
                if curr.child:
                    if curr.next:
                        stack.append(curr.next)
                    curr.next = curr.child
                    curr = curr.child
                    curr.prev = prev
                    prev.child = None
                    
                else:
                    curr = curr.next

        dummy.next = None
        head.prev = None

        return head
            
            
            