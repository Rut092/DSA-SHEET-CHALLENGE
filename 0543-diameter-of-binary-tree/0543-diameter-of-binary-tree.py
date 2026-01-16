# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = 0

        def diameter(root):
            if root==None:
                return 0
            else:
                left = diameter(root.left)
                right = diameter(root.right)

                self.maxi = max(self.maxi,left+right)

                return 1+max(left,right)

        diameter(root)
        return self.maxi