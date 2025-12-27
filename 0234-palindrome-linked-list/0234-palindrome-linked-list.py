# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        pointer = head
        while(pointer!=None):
            stack.append(pointer.val)
            pointer = pointer.next
        i,j=0,len(stack)-1
        while(i<j):
            if stack[i]==stack[j]:
                i+=1
                j-=1
            else:
                return False
        return True