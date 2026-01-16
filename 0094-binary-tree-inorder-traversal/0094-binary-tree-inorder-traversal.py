# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        stack = [[root,1]]
        while(stack):
            node,count = stack.pop()
            if count==2:
                ans.append(node.val)
            else:
                if node.right:
                    stack.append([node.right,1])
                stack.append([node,2])
                if node.left:
                    stack.append([node.left,1])

        return ans
