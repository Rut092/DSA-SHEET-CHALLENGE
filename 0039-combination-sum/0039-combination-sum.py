class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        def calc(index,total,val):
            if total==target:
                res.append(val)
                return
            if total>target or index==l:
                return
            
            calc(index,total+nums[index],val+[nums[index]])
            calc(index+1,total,val)

        calc(0,0,[])
        return res