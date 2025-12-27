# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = fast = head

        while(fast and fast.next):
            if fast.next.next:
                slow = slow.next
            fast=fast.next.next
            
        prev,pointer = None,slow.next
        
        while(pointer):
            forward = pointer.next
            pointer.next=prev
            prev = pointer
            pointer =forward
        
        pointer=head
        
        while(prev):
            if prev.val!=pointer.val:
                return False
            prev=prev.next
            pointer = pointer.next
        return True
