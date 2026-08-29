class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = (10**9+7)
        next = (self.nextSmaller(arr))
        prev = (self.prevSmaller(arr))
        total = 0
        for i in range(len(arr)):
            left = i-prev[i]
            right = next[i]-i
            total = (total + left*right*arr[i])%mod

        return total

    def nextSmaller(self,arr):
        l = len(arr)
        res = []
        stack = []

        for i in range(l-1,-1,-1):
            while(stack and arr[stack[-1]]>arr[i]):
                stack.pop()
            ele = l if not stack else stack[-1]
            stack.append(i)
            res.append(ele)
        return res[::-1]
    

    def prevSmaller(self,arr):
        l = len(arr)
        res = []
        stack = []

        for i in range(l):
            while(stack and arr[stack[-1]]>=arr[i]):
                stack.pop()
            ele = -1 if not stack else stack[-1]
            stack.append(i)
            res.append(ele)
        return res