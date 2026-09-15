class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = l = r = 0
        length = len(nums)

        while(r<length-1):
            farthest = 0
            for ind in range(l,r+1):
                farthest = max(ind+nums[ind],farthest)
            jumps+=1
            l = r+1
            r = farthest
        
        return jumps