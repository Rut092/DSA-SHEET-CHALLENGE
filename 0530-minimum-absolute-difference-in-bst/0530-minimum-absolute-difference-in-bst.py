# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        min_count = prev = float('inf')
        stack = []
        curr = root

        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            min_count = min(min_count,abs(prev-curr.val))
            prev = curr.val

            curr = curr.right

        return min_count