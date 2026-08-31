class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        maxi = 0
        stack = []
        for i in range(l):
            while(stack and heights[stack[-1]]>heights[i]):
                ele_idx = stack.pop()
                nse = i
                pse = -1 if not stack else stack[-1]
                maxi = max(maxi,(nse-pse-1)*heights[ele_idx])

            stack.append(i)

        while(stack):
            ele_idx = stack.pop()
            nse = l
            pse = -1 if not stack else stack[-1]
            maxi = max(maxi,(nse-pse-1)*heights[ele_idx])

        return maxi