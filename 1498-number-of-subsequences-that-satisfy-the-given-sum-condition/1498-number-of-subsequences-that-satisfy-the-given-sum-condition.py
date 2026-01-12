class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        count = 0
        length = len(nums)
        i,j=0,length-1
        mod = (10**9+7)
        power = [1]*length

        for k in range(1, length):
            power[k] = (power[k-1] * 2) % mod

        while(i<=j):
            if nums[i]+nums[j]>target:
                j-=1
            else:
                count=  (count + power[j-i])%mod
                i+=1
        return count

        