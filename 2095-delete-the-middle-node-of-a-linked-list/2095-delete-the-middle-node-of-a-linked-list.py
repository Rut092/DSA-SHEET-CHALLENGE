# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        fast = slow = head
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next
        else:
            return None
        
        return head