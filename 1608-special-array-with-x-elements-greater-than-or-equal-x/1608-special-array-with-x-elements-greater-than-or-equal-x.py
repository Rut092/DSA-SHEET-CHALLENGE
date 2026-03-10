class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = len(nums)
        low,high = 0,l
        while(low<=high): 
            mid = (low+high)//2
            count = 0

            for num in nums:
                if num>=mid:
                    count+=1

            if count==mid:
                return mid
            elif count>mid:
                low = mid+1
            else:
                high = mid-1

        return -1