# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        sorted_arr = []
        stack = []
        curr = root
        while(stack or curr):
            while(curr):
                stack.append(curr)
                curr=curr.left

            curr = stack.pop()
            sorted_arr.append(curr.val)
            curr = curr.right

        max_count = -1
        max_count_ele = []
        count=1
        ele = sorted_arr[0]
        for i in range(1,len(sorted_arr)):
            if sorted_arr[i-1]==sorted_arr[i]:
                count+=1
            else:
                if count>max_count:
                    max_count=count
                    max_count_ele = [ele]
                elif count==max_count:
                    max_count_ele.append(ele)
                ele = sorted_arr[i]
                count=1
        if count==max_count:
            max_count_ele.append(ele)
        elif count>max_count:
            max_count_ele=[ele]
        return max_count_ele