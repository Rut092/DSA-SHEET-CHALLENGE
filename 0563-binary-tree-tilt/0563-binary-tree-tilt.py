# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        def simplify(root):
            left_sum = 0
            right_sum = 0

            if root.left:
                left_sum = simplify(root.left)
            if root.right:
                right_sum = simplify(root.right)

            original = root.val
            root.val = abs(left_sum - right_sum)

            return left_sum + right_sum + original

        simplify(root)

        stack = [root]
        total = 0
        while(stack):
            node = stack.pop()
            total+=node.val

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


        return total