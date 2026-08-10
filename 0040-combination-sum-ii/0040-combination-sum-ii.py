class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(nums)<target:
            return []
        res = []
        l = len(nums)
        nums.sort()
        def calc(index,total,val):
            if total==target:
                res.append(val)
                return True
            if total>target or index==l:
                return False
            
            a = calc(index+1,total+nums[index],val+[nums[index]])
            while(a and index+1<l and nums[index]==nums[index+1]):
                index+=1
            b = calc(index+1,total,val)

            return a or b

        calc(0,0,[])
        res.sort()
        return res
        