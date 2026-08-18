class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # def calc(index,value):
        #     if index==len(nums):
        #         res.append(value)
        #         return
        #     calc(index+1,value)
        #     calc(index+1,value+[nums[index]])
        
        # calc(0,[])

        # Using Bit Manipulation
        n = len(nums)
        subsets = (1<<n)
        for num in range(subsets):
            array = []
            for i in range(n):
                if num&(1<<i):
                    array.append(nums[i])
            res.append(array)
        return res