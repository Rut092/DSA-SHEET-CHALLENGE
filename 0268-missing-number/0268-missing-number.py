class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        xor = len(nums)
        for i in range(xor):
            xor^=nums[i]
            xor^=i
        return xor