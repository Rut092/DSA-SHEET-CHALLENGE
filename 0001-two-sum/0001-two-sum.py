class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in key:
                return [key[val],i]
            key[nums[i]] = i
        
