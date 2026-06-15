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
        if not root : return 0
        
        left = self.height(root,True)
        right = self.height(root,False)

        if left == right:
            return 2**(left) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def height(self,node,left = True):

        count = 0
        if left:
            while(node):
                node=node.left
                count+=1
        else:
            while(node):
                node = node.right
                count+=1

        return count