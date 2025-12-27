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
            print(slow.val)
            if fast.next.next:
                slow = slow.next
            fast=fast.next.next
            
        pointer = head
        prev = None
        pointer = slow.next
        while(pointer):
            current = pointer
            forward = pointer.next
            current.next=prev
            prev = current
            pointer =forward
        
        slow = prev
        pointer=head
        while(slow):
            print(pointer.val,slow.val)
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