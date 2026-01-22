# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        sorted_arr = []
        stack = []
        curr = root
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            sorted_arr.append(curr.val)

            curr=curr.right
            
        i,j=0,len(sorted_arr)-1
        while(i<j):
            total = sorted_arr[i]+sorted_arr[j]
            if total==k:
                return True
            elif total<k:
                i+=1
            else:
                j-=1

        return False
        
        # book = set()
        # stack = [root]
        # while(stack):
        #     node = stack.pop()
        #     if k-node.val in book:
        #         return True
        #     book.add(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)

        # return False