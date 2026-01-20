# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = deque([[root,1]])
        
        while(stack):
            node,value = stack.popleft()

            if not node.left and not node.right:
                return value

            if node.left:
                stack.append([node.left,value+1])

            if node.right:
                stack.append([node.right,value+1])


