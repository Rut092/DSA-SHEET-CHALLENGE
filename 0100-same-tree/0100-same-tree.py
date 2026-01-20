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
        
        p_inorder = [p.val]
        q_inorder = [q.val]

        stack = [p]
        while(stack):
            node = stack.pop()

            if node:
                stack.append(node.right)
                stack.append(node.left)
            
            if node:
                p_inorder.append(node.val)
            else:
                p_inorder.append(None)
        
        stack = [q]
        while(stack):
            node = stack.pop()

            if node:
                stack.append(node.right)
                stack.append(node.left)
            
            if node:
                q_inorder.append(node.val)
            else:
                q_inorder.append(None)

        return p_inorder==q_inorder
        

