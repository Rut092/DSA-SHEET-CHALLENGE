# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next : return head

        mid_prev = self.middle(head)
        middle = mid_prev.next
        mid_prev.next = None

        left,right = self.sortList(head),self.sortList(middle)
        return self.conquer(left,right)

    def conquer(self,left,right):
        node = ListNode(0)
        curr = node
        while(left and right):
            if left.val<right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return node.next

    def middle(self,linkedList):
        fast,slow = linkedList.next,linkedList
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow
        


        