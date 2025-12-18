class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = []
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                for j in range(i+1,len(nums)-1):
                    if nums[j]>nums[j+1]:
                        return False
                
                if nums[-1]>nums[0]:
                    return False
                break

        return True