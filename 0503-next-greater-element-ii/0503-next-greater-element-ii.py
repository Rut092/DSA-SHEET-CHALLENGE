class Solution(object):
    def nextGreaterElements(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(arr)
        stack = []
        res = []
        for j in range(2):
            for i in range(l-1,-1,-1):
                curr = arr[i]
                while(stack and stack[-1]<=curr):
                    stack.pop()
                ele = -1 if not stack else stack[-1]
                stack.append(curr)
                res.append(ele)
            
        return res[-1:l-1:-1]