class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        left = current_sum = 0
        ans = float('inf')
        for right in range(l):
            current_sum+= nums[right]
            while(current_sum>=target):
                ans = min(ans,right-left+1)
                current_sum-=nums[left]
                left+=1

        return ans if ans!=float('inf') else 0