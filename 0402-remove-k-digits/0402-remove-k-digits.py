class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        l = len(num)
        tot = l-k
        if k-l==0: 
            return '0'
        stack = []
        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        res = "".join(stack[:tot]).lstrip('0')
        return res if res else "0"