class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = total = nums[0]
        for idx in range(1,len(nums)):
            if total<0:
                total=nums[idx]
            else:
                total+=nums[idx]
            max_total = max(max_total,total)
        return max_total
            