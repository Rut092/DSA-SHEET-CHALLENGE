# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        paths = []

        def getPaths(root):

            arr = []
            stack = [root]
            while(stack):
                node = stack.pop()
                if node:
                    arr.append(str(node.val))
                    stack.append(node.right)
                    stack.append(node.left)
                else:
                    arr.append('+')

            paths.append(arr)

        getPaths(root)
        getPaths(subRoot)

        haystack = paths[0]
        needle = paths[1]
        n_len,h_len=len(needle),len(haystack)
        lps = [0]*n_len

        prevLPS,i=0,1
        while(i<n_len):
            if needle[i]==needle[prevLPS]:
                lps[i]=prevLPS + 1
                i+=1
                prevLPS+=1

            elif prevLPS==0:
                lps[i]=0
                i+=1
            else:
                prevLPS = lps[prevLPS-1]
        
        i,j=0,0

        while(i<h_len):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]

            if j==n_len:
                return True

        return False

