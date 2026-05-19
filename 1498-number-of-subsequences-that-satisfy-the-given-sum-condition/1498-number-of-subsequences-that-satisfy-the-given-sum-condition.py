class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        mod = 10**9 + 7

        i,j=0,l-1
        count=0

        while(i<=j):
            if nums[i]+nums[j]<=target:
                count = (count + 2**(j-i))%mod
                i+=1
            else:
                j-=1
        return count