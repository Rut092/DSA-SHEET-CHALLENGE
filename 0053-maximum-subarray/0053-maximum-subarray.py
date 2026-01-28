class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = total = nums[0]
        for idx in range(1,len(nums)):
            if total+nums[idx]<total and total<0:
                max_total = max(max_total,nums[idx])
                total = nums[idx]
            elif total<0 and nums[idx]>=0:
                total=nums[idx]
                max_total = max(max_total,total)
            else:
                total+=nums[idx]
                max_total = max(max_total,total)
        return max_total
            