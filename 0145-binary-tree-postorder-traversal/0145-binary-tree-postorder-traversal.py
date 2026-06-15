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

        if not root : return []
        res = []
        stack = []
        curr = root
        visited = None

        while(curr or stack):
            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]
            if peek.right and peek.right!=visited:
                curr = peek.right
            else:
                node = stack.pop()
                res.append(node.val)
                visited = node

        return res