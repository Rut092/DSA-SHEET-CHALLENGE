# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return -1

        first = float('inf')
        second = float('inf')
        stack = [root]

        while(stack):
            node = stack.pop()
            if node.val<first:
                second = first
                first = node.val
            elif node.val<second and node.val>first:
                second = node.val

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return second if second!= float('inf') else -1