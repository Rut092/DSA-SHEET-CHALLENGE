# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        link = head
        link_end = None
        new_head = None
        prev = None
        count = 1
        curr = head
        while(curr.next):
            count+=1
            curr = curr.next

        curr = head

        for i in range(count//k):
            for j in range(k):
                if j==0:
                    link_end = link
                    link = curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            if new_head == None: new_head = prev
            link.next = curr
            link_end.next = prev
            prev = None

        link.next = curr

        return new_head
