class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        l = len(nums)
        high = l-1

        while(low<high):
            mid = (low+high)>>1
            if nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid

        return high