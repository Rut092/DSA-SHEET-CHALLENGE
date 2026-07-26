class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low,high = 0,sum(nums)
        while(low<=high):
            mid = (low+high)>>1
            
            if self.isPossible(nums,k,mid):
                high = mid-1
            else:
                low = mid+1

        return low

    def isPossible(self,nums,k,max_sum):
        count = 1
        curr_sum = 0
        for num in nums:
            if num>max_sum:
                return False
            elif curr_sum+num<=max_sum:
                curr_sum+=num
            else:
                count+=1
                curr_sum = num
                if count>k:
                    return False
            
        return True