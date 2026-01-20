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
            
            print(nodeP,"---",nodeQ)
            if ((nodeP==None or nodeQ==None) and nodeP!=nodeQ) or (nodeP!=None and nodeQ!=None and nodeP.val!=nodeQ.val):
                return False

            if nodeP and nodeQ:
                stack_p.append(nodeP.right)
                stack_q.append(nodeQ.right)

                stack_p.append(nodeP.left)
                stack_q.append(nodeQ.left)
    
        
        return True
        

