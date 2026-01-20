# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def binary_val(min_ind,max_ind):
            if min_ind<=max_ind:
                mid = (min_ind+max_ind)//2
                node = TreeNode(nums[mid])

                node.left = binary_val(min_ind,mid-1)
                node.right = binary_val(mid+1,max_ind)

                return node

            return None

        return binary_val(0,len(nums)-1)
            
