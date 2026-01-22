# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        curr = root
        min_val = float('inf')
        prev = float('inf')
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            min_val = min(min_val,abs(curr.val-prev))
            prev = curr.val

            curr = curr.right

        return min_val
