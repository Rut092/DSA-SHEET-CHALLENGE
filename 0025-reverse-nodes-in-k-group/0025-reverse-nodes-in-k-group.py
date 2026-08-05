# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head
        total = 0
        while(curr):
            total+=1
            curr = curr.next
        rev_tot = total//k

        new_head = ListNode(-1)
        new_curr = new_head
        front_node = None
        curr = head
        prev = None
        count = 0

        while(rev_tot):
            if count<k:
                if count==0:
                    front_node = curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count+=1
            else:
                count = 0
                rev_tot-=1
                new_curr.next = prev
                front_node.next = curr
                new_curr = front_node
                prev = None

        return new_head.next