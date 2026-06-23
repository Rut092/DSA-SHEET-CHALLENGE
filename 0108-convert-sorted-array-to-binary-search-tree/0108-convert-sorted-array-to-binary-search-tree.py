# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        def bin(min_ind,max_ind):
            if min_ind<=max_ind:
                mid = (min_ind+max_ind)>>1
                node = TreeNode(nums[mid])
                node.left = bin(min_ind,mid-1)
                node.right = bin(mid+1,max_ind)

                return node
        
        return bin(0,len(nums)-1)