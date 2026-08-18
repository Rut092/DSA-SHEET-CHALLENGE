class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thief = 0
        for i in range(31,-1,-1):
            count = 0
            for num in nums:
                if (num>>i)&1==1:
                    count+=1
            count%=3
            thief = thief<<1 | count
        
        if thief>=(1<<31): thief-=(1<<32)
        return thief