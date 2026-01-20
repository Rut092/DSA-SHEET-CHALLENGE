# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p or not q:
            if p==q:
                return True
            return False
        
        stack = [[p,q]]

        while(stack):
            nodeP,nodeQ = stack.pop()
    
            if (nodeP.val!=nodeQ.val):
                return False

            if nodeP and nodeQ:
                if nodeP.right and nodeQ.right:
                    stack.append([nodeP.right,nodeQ.right])

                elif nodeP.right!=nodeQ.right:
                    return False

                if nodeP.left and nodeQ.left:
                    stack.append([nodeP.left,nodeQ.left])

                elif nodeP.left!=nodeQ.left:
                    return False

        return True
        

