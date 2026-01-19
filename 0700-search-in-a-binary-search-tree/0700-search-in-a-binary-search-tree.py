# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        subroot = None
        while(root):
            if root.val == val:
                subroot = root
                break
            elif root.val>val:
                root = root.left
            else:
                root=root.right
        return subroot