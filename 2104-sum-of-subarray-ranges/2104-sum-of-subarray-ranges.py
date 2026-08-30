class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small_left = (self.prevSmaller(nums))
        small_right = (self.nextSmaller(nums))
        large_left = (self.prevLarger(nums))
        large_right = (self.nextLarger(nums))
        total = 0

        for i in range(len(nums)):
            s_l,s_r = i - small_left[i],small_right[i] - i
            r_l,r_r = i - large_left[i],large_right[i] - i

            small = s_l*s_r*nums[i]
            large = r_l*r_r*nums[i]

            total+= (large-small)

        return total
        
    def nextLarger(self,nums):
        l = len(nums)
        res,stack=[],[]
        for i in range(l-1,-1,-1):
            while(stack and nums[stack[-1]]<nums[i]):
                stack.pop()
            ele = l if not stack else stack[-1]
            stack.append(i)
            res.append(ele)
        return res[::-1]

    def prevSmaller(self,nums):
        res,stack=[],[]
        for i in range(len(nums)):
            while(stack and nums[stack[-1]]>=nums[i]):
                stack.pop()
            ele = -1 if not stack else stack[-1]
            stack.append(i)
            res.append(ele)
        return res

    def prevLarger(self,nums):
        res,stack=[],[]
        for i in range(len(nums)):
            while(stack and nums[stack[-1]]<=nums[i]):
                stack.pop()
            ele = -1 if not stack else stack[-1]
            stack.append(i)
            res.append(ele)
        return res

    def nextSmaller(self,nums):
        l = len(nums)
        res,stack=[],[]
        for i in range(l-1,-1,-1):
            while(stack and nums[stack[-1]]>nums[i]):
                stack.pop()
            ele = l if not stack else stack[-1]
            stack.append(i)
            res.append(ele)

        return res[::-1]