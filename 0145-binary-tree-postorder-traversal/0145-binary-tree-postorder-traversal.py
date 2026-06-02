# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []
        stack = []
        curr = root
        visited = None

        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left
            
            node = stack[-1]
            if node.right and visited!=node.right:
                curr = node.right
            else:
                visited = stack.pop()
                res.append(visited.val)

        return res