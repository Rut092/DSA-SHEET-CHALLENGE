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
        reach = 0
        while(idx<l and reached[idx]):
            for i in range(reach,nums[idx]+1+idx):
                if i<l-1:
                    reached[i]=1
                    reach = i-1
                else:
                    return True
            idx+=1
        return False
