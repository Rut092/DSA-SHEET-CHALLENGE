# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        curr_sum = 0
        q = deque([[root,root.val]])

        while(q):
            l = len(q)
            for i in range(l):
                node,val = q.popleft()
                if node.left or node.right:
                    if node.left:
                        q.append([node.left,val<<1|node.left.val])
                    if node.right:
                        q.append([node.right,val<<1|node.right.val])
                else:
                    curr_sum+=val
        return curr_sum