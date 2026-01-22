# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        book = {}
        stack = [root]
        while(stack):
            node = stack.pop()
            if k-node.val in book:
                return True
            book[node.val]=0
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False