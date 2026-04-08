# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        curr = head
        while(curr and curr.next):
            curr = curr.next
            count+=1

        k = k%count
        
        if k==0: return head

        end = head
        mid = head

        for i in range(k):
            end = end.next

        while(end.next):
            end = end.next
            mid = mid.next
        
        new_head = mid.next
        end.next = head
        mid.next = None

        return new_head