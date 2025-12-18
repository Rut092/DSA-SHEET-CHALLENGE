class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = []
        for i in range(len(nums)-1):
            print(i,'i')
            if nums[i]>nums[i+1]:
                last =-1
                for j in range(i+1,len(nums)):
                    print(j,'j')
                    if j<len(nums)-1 and nums[j]>nums[j+1]:
                        return False
                    else:
                        last = nums[j]
                
                if last>nums[0]:
                    return False
                return True

        return True