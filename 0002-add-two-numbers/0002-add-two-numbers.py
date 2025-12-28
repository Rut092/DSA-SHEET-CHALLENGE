# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        prev = None
        node1,node2 = l1,l2

        while(node1 and node2):
            total = carry + node1.val + node2.val
            node1.val = total%10
            carry = total//10
            prev = node1
            node1,node2 = node1.next,node2.next
        
        while(node1 and carry):
            total = carry + node1.val
            node1.val = total%10
            carry = total//10
            prev = node1
            node1= node1.next

        if node2:
            prev.next=node2

        while(node2 and carry):
            total = carry + node2.val
            node2.val = total%10
            carry = total//10
            prev = node2
            node2= node2.next
        
        if carry:
            prev.next = ListNode(carry)
        
        return l1
