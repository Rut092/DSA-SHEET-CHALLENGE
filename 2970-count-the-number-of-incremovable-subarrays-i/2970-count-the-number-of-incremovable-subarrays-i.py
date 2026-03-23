class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        valid_from_right = -1
        valid_from_left = l

        for i in range(1,l):
            if nums[i-1]>=nums[i]:
                valid_from_left = i
                break

        if valid_from_left == l:
            return (l*(l+1))//2

        for i in range(l-2,-1,-1):
            if nums[i+1]<=nums[i]:
                valid_from_right = i+1
                break
        
        count = valid_from_left + 1 + l - valid_from_right

        for i in range(valid_from_left):
            while valid_from_right<l and nums[i]>=nums[valid_from_right]:
                valid_from_right+=1
            count+=(l-valid_from_right)

        return count