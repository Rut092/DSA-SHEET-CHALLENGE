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
        
        stack_p = [p]
        stack_q = [q]

        while(stack_p and stack_q):
            nodeP = stack_p.pop()
            nodeQ = stack_q.pop()
            
            if (nodeP.val!=nodeQ.val):
                return False

            if nodeP and nodeQ:
                if nodeP.right and nodeQ.right:
                    stack_p.append(nodeP.right)
                    stack_q.append(nodeQ.right)
                elif nodeP.right!=nodeQ.right:
                    return False

                if nodeP.left and nodeQ.left:
                    stack_p.append(nodeP.left)
                    stack_q.append(nodeQ.left)
                elif nodeP.left!=nodeQ.left:
                    return False
    
        
        return True
        

