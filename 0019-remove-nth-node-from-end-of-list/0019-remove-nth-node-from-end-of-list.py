# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 0
        ptr = head
        while(n):
            ptr = ptr.next
            n-=1

        node = head
        prev = None
        while(ptr):
            ptr = ptr.next
            prev = node
            node = node.next
        
        if prev:
            prev.next = node.next
            return head
        if node:
            return head.next
        return None