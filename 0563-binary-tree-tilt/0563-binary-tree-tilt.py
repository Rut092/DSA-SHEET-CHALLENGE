# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        
        self.total = 0

        def simplify(root):

            left = 0 if not root.left else simplify(root.left)
            right = 0 if not root.right else simplify(root.right)

            data = root.val 

            root.data = abs(left-right)
            self.total+=root.data
        
            return data + left + right

        simplify(root)
        return self.total