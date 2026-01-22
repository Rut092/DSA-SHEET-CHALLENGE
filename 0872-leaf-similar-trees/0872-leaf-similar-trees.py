# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        res = deque()
        stack = [root1]
        while(stack):
            node = stack.pop()
            if node.left and node.right:
                stack.append(node.right)
                stack.append(node.left)
            elif node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
            else:
                res.append(node.val)
        
        stack = [root2]
        while(stack):
            node = stack.pop()
            if node.left and node.right:
                stack.append(node.right)
                stack.append(node.left)
            elif node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
            else:
                if not res or res.popleft()!=node.val:
                    return False

        return True if not res else False
        

        