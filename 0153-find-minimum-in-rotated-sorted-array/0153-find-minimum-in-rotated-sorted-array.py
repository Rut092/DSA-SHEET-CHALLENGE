class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_int = 2**32

        low,high = 0,len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                max_int = min(max_int,nums[low])
                low=mid+1
            else:
                max_int = min(max_int,nums[mid])
                high=mid-1

        return max_int 


                