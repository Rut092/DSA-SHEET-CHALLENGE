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
        if not head.next: return None
        end = head
        for _ in range(n):
            end = end.next
        
        if end == None:
            return head.next
            
        curr = head
        while(end.next):
            end = end.next
            curr = curr.next
        
        curr.next = curr.next.next

        return head