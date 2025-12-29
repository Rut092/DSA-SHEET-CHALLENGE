class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        m=j=len(nums)
        while(m):
            index = (i+j)//2
            if nums[index]==target:
                return index
            elif nums[index]>target:
                j = index
            else:
                i = index
            m//=2
        return -1