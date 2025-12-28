class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ele = None
        for num in nums:
            if count==0:
                ele = num
            
            count+=1 if ele==num else -1
        return ele
