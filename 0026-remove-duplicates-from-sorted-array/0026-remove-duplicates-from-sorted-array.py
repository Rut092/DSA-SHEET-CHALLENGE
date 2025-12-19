class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        for j in range(1,l):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
        return i+1