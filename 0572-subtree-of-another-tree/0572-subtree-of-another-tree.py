# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        needle = self.getPaths(subRoot)
        heystack = self.getPaths(root)

        n_len,h_len = len(needle),len(heystack)
        lps = [0]*n_len
        prevLPS,i = 0,1
        
        while(i<n_len):
            if needle[i]==needle[prevLPS]:
                lps[i] = prevLPS + 1
                i+=1
                prevLPS+=1
            
            elif prevLPS==0:
                lps[i]=0
                i+=1
            else:
                prevLPS = lps[prevLPS - 1]

        i,j = 0,0
        while(j<h_len):
            if needle[i]==heystack[j]:
                i+=1
                j+=1
            else:
                if i==0:
                    j+=1
                else:
                    i = lps[i-1]
            
            if i==n_len:
                return True

        return False

    def getPaths(self,root):
        path = []
        stack = [root]
        while(stack):
            node = stack.pop()
            if node:
                path.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                path.append('#')
        
        return path