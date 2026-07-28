class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        curr_sum = left = 0
        ans = float('inf')
        for right in range(l):
            curr_sum+=nums[right]
            while(curr_sum>=target):
                ans = min(ans,right-left)
                curr_sum-=nums[left]
                left+=1
        
        return ans+1 if ans!=float('inf') else 0