class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        pse,nse = self.pse(heights,l),self.nse(heights,l)
        maxi = 0
        for i in range(l):
            maxi = max(maxi,(nse[i]-pse[i]-1)*heights[i])
        return maxi


    def nse(self,height,l):
        res,stack =[],[]
        for i in range(l-1,-1,-1):
            while(stack and height[stack[-1]]>height[i]):
                stack.pop()
            curr = l if not stack else stack[-1]
            res.append(curr)
            stack.append(i)
        return res[::-1]

    def pse(self,height,l):
        res,stack = [],[]
        for i in range(l):
            while(stack and height[stack[-1]]>=height[i]):
                stack.pop()
            curr = -1 if not stack else stack[-1]
            res.append(curr)
            stack.append(i)
        return res