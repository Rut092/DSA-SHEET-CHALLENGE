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
        count = 0
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
                if count>max_ele_count:
                    max_ele_count = count
                    max_ele = [ele]
                
                elif count==max_ele_count:
                    max_ele.append(ele)
                
                ele=curr.val
                count=1
            
            curr = curr.right

        if count==max_ele_count:
            max_ele.append(ele)
        elif count>max_ele_count:
            max_ele=[ele]

        return max_ele