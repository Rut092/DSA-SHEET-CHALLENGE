import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = len(nums)
        low,high = 1,max(nums)
        
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            val = self.calc(nums,mid)
            print(low,mid,high,val)

            if val>threshold:
                
                low = mid+1
            else:
                ans = mid
                high = mid-1

        return ans

    def calc(self,nums,ele):
        total = 0
        for num in nums:
            total+=math.ceil(num/ele)
        return total
