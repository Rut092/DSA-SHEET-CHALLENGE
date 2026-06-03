# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0

        left = self.left_height(root)
        right = self.right_height(root)

        if left==right:
            return 2**left-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def left_height(self,root):
        height = 0
        curr = root
        while(curr):
            height+=1
            curr = curr.left
        return height
    
    def right_height(self,root):
        height = 0
        curr = root
        while(curr):
            height+=1
            curr = curr.right
        return height