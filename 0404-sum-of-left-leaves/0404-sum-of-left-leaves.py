# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [[root,0]]
        total = 0
        while(stack):
            node,is_left = stack.pop()
            
            if not node.left and not node.right and is_left:
                total+=node.val
             
            if node.right:
                stack.append([node.right,0])  
            if node.left:
                stack.append([node.left,1])
                
        return total