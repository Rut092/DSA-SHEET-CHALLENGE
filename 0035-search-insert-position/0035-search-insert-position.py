class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j=0,len(nums)-1
        while(i<=j):
            index = (i+j)//2
            if nums[index]==target:
                return index
            elif nums[index]<target:
                i = index+1
            else:
                j = index-1
        return i