class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
            if count[i] > l/2:
                return i
