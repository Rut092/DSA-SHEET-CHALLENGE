# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        total = 0
        stack = []
        curr = root
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if low<=curr.val<=high:
                total+=curr.val
            elif curr.val>high:
                return total
            
            curr = curr.right

        return total
            