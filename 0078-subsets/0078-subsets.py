class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []


        def calc(index,value):
            if index==len(nums):
                res.append(value)
                return
            calc(index+1,value)
            calc(index+1,value+[nums[index]])
        
        calc(0,[])
        print(res)
        return list(res)