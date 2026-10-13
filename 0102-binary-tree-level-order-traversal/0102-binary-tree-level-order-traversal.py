# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        q = deque([[root,1]] if root else [])
        level = 1
        while(q):
            curr_res = []
            while(q and q[0][1]==level):
                node,level = q.popleft()
                
                if node.left:
                    q.append([node.left,level+1])
                if node.right:
                    q.append([node.right,level+1])
                
                curr_res.append(node.val)

            level+=1
            res.append(curr_res)
        
        return res