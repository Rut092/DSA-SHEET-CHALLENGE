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
        dummy = ListNode(0)
        dummy.next = head
        prev = None
        slow = dummy
        fast = head
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        slow.next  = slow.next.next
        
        return dummy.next