# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        depth = 0
        count = 0
        num = 0
        q = deque([[root,0]])
        while(q):
            node,level = q.popleft()

            if level == depth:
                count+=node.val
                num+=1
            else:
                depth+=1
                res.append(count/num)
                num=1
                count=node.val

            if node.left:
                q.append([node.left,level+1])
            if node.right:
                q.append([node.right,level+1])

        res.append(count/num)
        return res