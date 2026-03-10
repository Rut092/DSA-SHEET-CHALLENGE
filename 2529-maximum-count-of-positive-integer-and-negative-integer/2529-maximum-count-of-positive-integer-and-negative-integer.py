class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        res = -1
        low = 0
        l = len(nums)
        high = l-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]<0:
                res = mid
                low = mid+1
            else:
                high = mid-1

        low = res 
        high = l-1
        zeros = res
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]<=0:
                zeros = mid
                low = mid+1
            else:
                high = mid-1
        return max(res+1,l-(res+1)-(zeros-res))