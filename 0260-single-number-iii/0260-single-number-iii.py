class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor = 0
        for num in nums:
            xor^=num
        xor&=(-xor)

        bucket1 = 0
        bucket2 = 0
        for num in nums:
            if num&xor==0:
                bucket1^=num
            else:
                bucket2^=num
        return [bucket1,bucket2]
                
