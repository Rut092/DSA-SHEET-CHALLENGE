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
        for i in range(l-2,-1,-1):
            if nums[i+1]<=nums[i]:
                valid_from_right = i
                break
        
        count = 0
        print(valid_from_left,valid_from_right)
        for i in range(l):
            for j in range(i,l):
                is_bridge = True
                if i>0 and j<l-1 and nums[i-1]>=nums[j+1]:
                    is_bridge = False
                count+=((i<=valid_from_left) and (j>=valid_from_right) and (is_bridge))
        return count