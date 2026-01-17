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
        if not root:
            return 0
        stack=[root]
        count=0
        while(stack):
            node = stack.pop()
            count+=1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return count
