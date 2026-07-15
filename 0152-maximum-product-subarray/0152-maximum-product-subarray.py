class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('-inf')
        pre = suff = 1
        l = len(nums)

        for i in range(l):
            pre*=nums[i]
            suff*=nums[l-i-1]

            maxi = max(maxi,pre,suff)

            if pre==0:
                pre=1
            if suff==0:
                suff = 1

        return maxi