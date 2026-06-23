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
        if not root : 
            return 0

        left = self.height(root,1)
        right = self.height(root,0)

        if left == right:
            return 2**(left)-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def height(self,root,is_left):
        count = 0
        while(root):
            count+=1
            if is_left:
                root = root.left
            else:
                root = root.right

        return count