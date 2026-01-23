# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        q = deque([root])
        while(q):
            length = len(q)
            i,j=0,length-1
            while(i<j):
                q[i].val,q[j].val=q[j].val,q[i].val
                i+=1
                j-=1

            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
