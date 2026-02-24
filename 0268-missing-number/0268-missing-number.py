class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        truth_xor = 0
        res_xor = nums[0]
        l = len(nums)
        for i in range(1,l):
            truth_xor^=i
            res_xor^=nums[i]
        return truth_xor^res_xor^l