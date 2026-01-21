# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        curr = root
        ele = root.val
        count,max_ele_count = 0,0
        max_ele = []
        max_ele_count = 0


        while(stack or curr):
            while(curr):
                stack.append(curr)
                curr=curr.left

            curr = stack.pop()
        
            if curr.val==ele:
                count+=1
            else:
                ele=curr.val
                count=1
            if count>max_ele_count:
                max_ele_count = count
                max_ele = [ele]
                
            elif count==max_ele_count:
                max_ele.append(ele)
            
            curr = curr.right

        return max_ele