class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        idx = -1
        for i in range(l-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx = i
                break
        
        if idx!=-1:
            for i in range(l-1,idx-1,-1):
                if nums[idx]<nums[i]:
                    nums[idx],nums[i]=nums[i],nums[idx]
                    break

        l-=1
        idx+=1
        while(idx<l):
            nums[idx],nums[l]=nums[l],nums[idx]
            idx+=1
            l-=1

        
        