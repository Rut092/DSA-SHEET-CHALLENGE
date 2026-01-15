class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        idx = reach = 0
        while(idx<l and reach>=idx):
            reach = max(reach,nums[idx]+idx)
            if reach>=l-1:
                return True
            idx+=1
        return False
