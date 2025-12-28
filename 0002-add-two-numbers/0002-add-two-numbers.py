# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p=None
        new=None
        carry=0
        while(l1 or l2):
            if l1 is None:
                m=0
            else:
                m=l1.val
                l1=l1.next
            if l2 is None:
                n=0
            else:
                n=l2.val
                l2=l2.next
            if m+n+carry>=10:
                q=(m+n+carry)%10
                carry=1
            else:
                q=m+n+carry
                carry=0
            if p is None:
                p=ListNode(q)
                new=p
            else:
                new.next=ListNode(q)
                new=new.next 
        if carry==1:
            new.next=ListNode(1)
        return p
            
        