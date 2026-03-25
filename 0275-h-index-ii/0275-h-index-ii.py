class Solution(object):
    def hIndex(self, nums):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(nums)
        low,high = 0,l-1
        ans = 0
        while(low<=high):
            mid = (low+high)//2
            
            if nums[mid]>=l-mid:
                ans = l-mid
                high = mid-1
            else:
                low = mid+1

        return ans
        