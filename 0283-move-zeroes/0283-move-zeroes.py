class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i=0
        j=0
        while(j<l):
            if nums[j]!=0 and nums[i]==0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            if nums[i]!=0:
                i+=1
            j+=1

        