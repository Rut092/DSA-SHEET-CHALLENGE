# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = float('inf')

        stack = [[root,1]]
        
        while(stack):
            node,value = stack.pop()

            if not node.left and not node.right:
                depth = min(depth,value)
    
            if node.right:
                stack.append([node.right,value+1])
            
            if node.left:
                stack.append([node.left,value+1])

        return depth


