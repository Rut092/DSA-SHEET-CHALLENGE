class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        idx = -1
        for i in range(l-1,0,-1):
            if nums[i-1]<nums[i]:
                idx = i-1
                break
        if idx!=-1:
            for i in range(l-1,idx-1,-1):
                if nums[idx]<nums[i]:
                    nums[idx],nums[i]=nums[i],nums[idx]
                    break
    
        idx+=1
        l-=1
        while(idx<l):
            nums[idx],nums[l]=nums[l],nums[idx]
            idx+=1
            l-=1
        

