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
        if not head : return head
        
        odd_head,even_head = head,head.next
        even = even_head

        while(even_head and even_head.next):

            odd_head.next = even_head.next
            odd_head = odd_head.next

            even_head.next = odd_head.next
            even_head = even_head.next

        odd_head.next = even

        return head



