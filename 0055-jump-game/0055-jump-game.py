class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        idx = 0
        reached = [0]*l
        reached[0]=1
        while(idx<l and reached[idx]):
            for i in range(nums[idx]+1):
                if idx+i<l-1:
                    reached[idx+i]=1
                else:
                    return True
            idx+=1
        return False
