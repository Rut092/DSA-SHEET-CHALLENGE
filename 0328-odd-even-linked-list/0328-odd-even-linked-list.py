# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next : return head
        odd_head,even_head = head,head.next
        odd,even = odd_head,even_head

        odd_flag = 1
        curr = head.next.next
        while(curr):
            if odd_flag:
                odd_flag = 0
                odd.next = curr
                odd = odd.next
            else:
                odd_flag = 1
                even.next = curr
                even = even.next

            curr = curr.next
            
        even.next = None
        odd.next = even_head
        return odd_head



