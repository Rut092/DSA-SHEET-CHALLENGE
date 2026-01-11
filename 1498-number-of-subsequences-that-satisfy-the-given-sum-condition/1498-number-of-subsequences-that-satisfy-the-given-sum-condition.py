class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)
        nums.sort()
        count = 0
        i,j=0,length-1
        mod = (10**9+7)

        while(i<=j):
            if nums[i]+nums[j]>target:
                j-=1
            else:
                count=(count+2**(j-i))%mod
                i+=1
        return count

        