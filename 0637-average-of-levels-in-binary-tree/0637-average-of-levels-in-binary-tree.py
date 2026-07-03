# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res = []
        q = deque([root])

        while(q):
            level_length = len(q)
            curr_sum = 0.0
            for i in range(level_length):
                node = q.popleft()
                curr_sum+=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(curr_sum/level_length)
        
        return res

