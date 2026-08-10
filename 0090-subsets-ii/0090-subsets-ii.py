class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        nums.sort()
        def calc(index,current):
            if index==l:
                res.append(current)
                return 

            calc(index+1,current+[nums[index]])
            
            while(index<l-1 and nums[index]==nums[index+1]):
                index+=1
            
            calc(index+1,current)

        calc(0,[])
        return res