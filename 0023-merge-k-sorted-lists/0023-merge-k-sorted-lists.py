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
        return self.divide(lists,0,len(lists)-1) if len(lists)>0 else None

    def divide(self,lists,start,end):
        if start==end:
            return lists[start]
        mid = (start+end)>>1
        print(start,end)
        left = self.divide(lists,start,mid)
        right = self.divide(lists,mid+1,end)

        return self.merge_lists(left,right)

    def merge_lists(self,list1,list2):
        dummy = ListNode(0)
        curr = dummy
        while(list1 and list2):
            if list1.val<list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        while(list1):
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while(list2):
            curr.next = list2
            curr = curr.next
            list2 = list2.next

        curr.next = None
        return dummy.next
