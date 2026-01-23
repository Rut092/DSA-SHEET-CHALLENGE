# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q = deque([root])
        x_pos,y_pos = None,None

        while(q):
            length = len(q)
            x_pos,y_pos = 0,0
            for i in range(length):
                node = q.popleft()
                same_root = 0
                if node.right:
                    if node.right.val==x:
                        x_pos = 1
                        same_root = 1
                    elif node.right.val==y:
                        y_pos = 1
                        same_root=1
                    q.append(node.right)
                
                if node.left:
                    if node.left.val==x and not same_root:
                        x_pos = 1
                    elif node.left.val==y and not same_root:
                        y_pos = 1
                    q.append(node.left)
                
            
            if x_pos and y_pos:
                return True
            elif x_pos or y_pos:
                return False
        
        return False