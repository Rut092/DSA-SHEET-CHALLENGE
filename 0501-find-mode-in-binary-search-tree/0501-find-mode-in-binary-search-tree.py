# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        res_ele,res_count = [],0
        temp_ele,temp_count = None,0     

        stack,curr = [],root
        while(stack or curr):
            while(curr):
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]
            if peek.right:
                curr = peek.right

            node = stack.pop()

            # check ele
            if node.val==temp_ele:
                temp_count+=1
            else:
                temp_count = 1
                temp_ele = node.val
                
            if res_count==temp_count:
                res_ele.append(temp_ele)
            elif res_count<temp_count:
                res_count = temp_count
                res_ele = [temp_ele]

        return res_ele