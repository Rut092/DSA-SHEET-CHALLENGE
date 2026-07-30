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

        evenDummy = ListNode(0)
        oddDummy = ListNode(0)
        curr_head = oddDummy
        even_head = evenDummy
        even = False
        while(head):
            if even:
                evenDummy.next = head
                evenDummy = evenDummy.next
                even = False
            else:
                oddDummy.next = head
                oddDummy = oddDummy.next
                even = True

            nxt = head.next
            head.next = None
            head = nxt
        
        oddDummy.next = even_head.next
        return curr_head.next
