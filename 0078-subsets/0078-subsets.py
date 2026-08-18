class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        subsets = (1<<n)
        for num in range(subsets):
            array = []
            for i in range(n):
                if num&(1<<i):
                    array.append(nums[i])
            res.append(array)
        return res