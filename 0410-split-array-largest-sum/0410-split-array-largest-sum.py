class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low,high = 0,sum(nums)
        while(low<=high):
            mid = (low+high)//2
            print(mid)
            if self.isPossible(nums,k,mid):
                high = mid-1
            else:
                low = mid+1

        return low

    def isPossible(self,nums,k,value):
        count = 1
        val = value
        for num in nums:
            if val-num>=0:
                val-=num
            elif value-num<0:
                return False
            else:
                val = value-num
                count+=1
                
        return count<=k