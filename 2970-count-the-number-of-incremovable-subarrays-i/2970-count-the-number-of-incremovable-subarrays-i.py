class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        left_valid = 0
        right_valid = l-1

        while(left_valid<l-1):
            if nums[left_valid]<nums[left_valid + 1]:
                left_valid+=1
            else:
                break
        
        if left_valid >=l-1: return l*(l+1)//2

        while(right_valid>0):
            if nums[right_valid]>nums[right_valid-1]:
                right_valid-=1
            else:
                break
        
        count = 1 + l - right_valid + left_valid+1
        for i in range(left_valid+1):
            while(right_valid<l and nums[i]>=nums[right_valid]):
                right_valid+=1
            count+= (l-right_valid)
        return count