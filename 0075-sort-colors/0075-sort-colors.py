class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i=0
        for j in range(length):
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        for j in range(i,length):
            if nums[j]==1:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                
