class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = -1,0
        l = len(nums)

        max_count = 0

        while(j<l):
            if nums[j]!=1:
                i=j
            max_count = max(max_count,j-i)
            j+=1
        return max_count