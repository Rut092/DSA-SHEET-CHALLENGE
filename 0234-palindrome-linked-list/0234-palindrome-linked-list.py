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
            slow = slow.next
            fast=fast.next.next
        
        pointer = head
        if slow==head:
            return True
        slow = slow.next
        if slow==None:
            return False
        while(slow):
            if slow.val==pointer.val:
                slow=slow.next
                pointer = pointer.next
            else:
                return False
        return True

        # stack = []
        # pointer = head
        # while(pointer!=None):
        #     stack.append(pointer.val)
        #     pointer = pointer.next
        # pointer = head
        # while(len(stack) and pointer.val==stack.pop()):
        #     pointer=pointer.next
        # return True if len(stack)==0 else False