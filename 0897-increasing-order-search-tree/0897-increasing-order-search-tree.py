# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = None
        if not root: return []
        rootmain = None
        stack  = []
        curr = root
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev==None:
                rootmain=TreeNode(curr.val)
                prev = rootmain
            else:
                prev.right=TreeNode(curr.val)
                prev = prev.right
            
            curr = curr.right
        return rootmain