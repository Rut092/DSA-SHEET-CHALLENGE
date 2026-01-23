# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        stack=[]
        curr = [root,0,0]
        while(curr[0] or stack):
            while(curr[0]):
                data = curr[1]<<1 | curr[0].val
                stack.append([curr[0],data])
                curr = [curr[0].left,data]

            curr = stack.pop()
            if not curr[0].left and not curr[0].right:
                total+=curr[1]

            curr = [curr[0].right,curr[1]]

        return total

            