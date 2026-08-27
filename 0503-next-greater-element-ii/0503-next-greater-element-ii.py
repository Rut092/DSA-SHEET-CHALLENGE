class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = nums+nums
        l = len(arr)
        stack = []
        res = []
        for i in range(l-1,-1,-1):
            curr = arr[i]
            while(stack and stack[-1]<=curr):
                stack.pop()
            ele = -1 if not stack else stack[-1]
            stack.append(curr)
            res.append(ele)
        
        return res[-1:len(nums)-1:-1]