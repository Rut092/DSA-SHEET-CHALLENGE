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
        slow,fast = head,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = head
        while(curr!=slow):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        if fast!=None: slow=slow.next
        while(slow):
            if prev.val!=slow.val:
                return False
            prev,slow=prev.next,slow.next
        
        return True
        