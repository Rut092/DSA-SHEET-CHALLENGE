# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d_head = ListNode(-101)
        prev = d_head

        while(head):
            if head.next and head.val==head.next.val:
                while(head.next and head.val==head.next.val):
                    head = head.next
            else:
                prev.next = head
                prev = prev.next

            head = head.next
        
        prev.next = None
        return d_head.next