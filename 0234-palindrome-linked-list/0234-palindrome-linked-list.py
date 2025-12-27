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
        stack = []
        pointer = head
        while(pointer!=None):
            stack.append(pointer.val)
            pointer = pointer.next
        pointer = head
        while(len(stack) and pointer.val==stack.pop()):
            pointer=pointer.next
        return True if len(stack)==0 else False