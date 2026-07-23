class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l==1 or nums[0]>nums[1]: return 0
        if nums[-1]>nums[-2]: return l-1

        low,high=1,l-1
        while(low<=high):
            mid = (low+high)>>1
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]:
                low = mid+1
            else:
                high = mid-1

        return l-1