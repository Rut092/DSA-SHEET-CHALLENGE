# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        n = len(lists)
        min_node = []
        for i in range(n):
            if (lists[i]):
                min_node.append([lists[i].val,lists[i]])

        heapq.heapify(min_node)
        dummy = ListNode(-1)
        curr = dummy

        while(min_node):
            _,node = heapq.heappop(min_node)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_node,[node.next.val,node.next])

        curr.next = None
        return dummy.next