class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0 
        n = len(nums)
        for i in nums:
            sum+=i
        series = ((n+1)*n)//2

        # if sum==series and l>1:
        #     return n
        return series-sum