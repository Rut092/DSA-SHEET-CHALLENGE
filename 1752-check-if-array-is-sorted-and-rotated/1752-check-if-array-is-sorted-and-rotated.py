class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        brk_pt = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                brk_pt+=1

        if len(nums)>1:
            if nums[0]<nums[-1]: brk_pt+=1

        return False if brk_pt>1 else True