class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        nums.sort()
        def calc(index,total,current):
            if total==target:
                res.append(current[:])
                return 
            
            for i in range(index,l):
                if i>index and nums[i-1]==nums[i]:
                    continue
                
                if total+nums[i]>target:
                    break

                current.append(nums[i])
                calc(i+1, total+nums[i],current)
                current.pop()
            
            
        calc(0,0,[])
        return res
        