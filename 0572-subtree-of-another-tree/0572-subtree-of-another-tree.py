# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isSame(root, subroot):
            stack = [[root, subroot]]
            while stack:
                node, subnode = stack.pop()

                if not node and not subnode:
                    continue
                if node and subnode and node.val == subnode.val:
                    stack.append([node.right, subnode.right])
                    stack.append([node.left, subnode.left])

                elif not node or not subnode or node.val != subnode.val:
                    return False

            return True

        def isPossibleSubroot(root, subRoot):
            stack = [root]
            while stack:
                node = stack.pop()

                if node.val == subRoot.val and isSame(node,subRoot):
                    return True

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        def isSame(root, subroot):
            stack = [[root, subroot]]
            while stack:
                node, subnode = stack.pop()

                if not node and not subnode:
                    continue
                if node and subnode and node.val == subnode.val:
                    stack.append([node.right, subnode.right])
                    stack.append([node.left, subnode.left])

                elif not node or not subnode or node.val != subnode.val:
                    return False

            return True

        if isPossibleSubroot(root, subRoot):
            return True
        return False
