class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = {}
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            curr = nums2[i]
            while(stack and stack[-1]<curr):
                stack.pop()
            ele = -1 if not stack else stack[-1]
            stack.append(curr)
            res[curr]=ele

        ans = []
        for i in nums1:
            ans.append(res[i])
        return ans