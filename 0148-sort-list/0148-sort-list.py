# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        mid_prev = self.mid(head)
        middle = mid_prev.next
        mid_prev.next = None

        left = self.sortList(head)
        right = self.sortList(middle)

        return self.conquer(left,right)

    def mid(self,start):
        slow = start
        fast = start.next
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        return slow

    
    def conquer(self,left,right):
        Dummy = ListNode(0)
        merged = Dummy

        while(left and right):
            if left.val>right.val:
                merged.next = right
                right = right.next
            else:
                merged.next = left
                left = left.next
                
            merged = merged.next
            merged.next = None

        while(left):
            merged.next = left
            left = left.next
            merged = merged.next
            merged.next = None

        while(right):
            merged.next = right
            right = right.next
            merged = merged.next
            merged.next = None

        return Dummy.next