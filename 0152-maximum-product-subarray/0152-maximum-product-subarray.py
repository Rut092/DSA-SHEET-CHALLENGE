class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        maxi=float('-inf')
        l = len(nums)
        for i in range(l):
            prefix*=nums[i]
            suffix*=nums[l-i-1]
            maxi=max(maxi,prefix,suffix)
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1

        return maxi