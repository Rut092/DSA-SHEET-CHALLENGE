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
        curr = [root,""]
        while(curr[0] or stack):
            while(curr[0]):
                string = curr[1]+str(curr[0].val)
                stack.append([curr[0],string])
                curr = [curr[0].left,string]

            curr = stack.pop()
            if not curr[0].left and not curr[0].right:
                total+=int(curr[1],2)

            curr = [curr[0].right,curr[1]]

        return total

            