# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 0
        ptr = head
        while(ptr):
            count+=1
            ptr = ptr.next
        count-=n

        if count==0: return head.next

        ptr = head
        count-=1
        while(count>0):
            count-=1
            ptr = ptr.next

        ptr.next = ptr.next.next if ptr.next.next else None
        
        return head