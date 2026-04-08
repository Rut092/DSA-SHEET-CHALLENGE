# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        group_prev = dummy

        count = 1
        curr = head
        while(curr.next):
            count+=1
            curr = curr.next

        curr = head
        for i in range(count//k):
            prev = None
            group_tail = curr

            for j in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            group_tail.next = curr
            group_prev.next = prev
            group_prev = group_tail

        return dummy.next
