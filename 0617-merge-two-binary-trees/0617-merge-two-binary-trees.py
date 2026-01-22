# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = [[root1,root2,None,-1]]

        while(stack):
            node1,node2,prev,left = stack.pop()

            if not node1 and not node2:
                continue

            if node1 and node2:
                node1.val+=node2.val
                stack.append([node1.right,node2.right,node1,0])
                stack.append([node1.left,node2.left,node1,1])

            elif node2 and prev:
                if not left:
                    prev.right=node2
                else:
                    prev.left=node2
            elif node2:
                return node2
        
        return root1