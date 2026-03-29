# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while(fast):
            if fast.next and fast.next.next:
                fast=fast.next.next
                slow = slow.next
                if fast==slow:
                    break
            else:
                return
                
        while(head!=slow):
            head = head.next
            slow = slow.next

        return slow