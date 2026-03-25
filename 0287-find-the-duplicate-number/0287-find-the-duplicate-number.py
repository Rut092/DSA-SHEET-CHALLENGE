class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        low,high = 1,l

        while(low<=high):
            mid = (low+high)//2
            count = 0

            for num in nums:
                if num<=mid:
                    count+=1

            if count>mid:
                high = mid-1
            else:
                low = mid+1

        return low