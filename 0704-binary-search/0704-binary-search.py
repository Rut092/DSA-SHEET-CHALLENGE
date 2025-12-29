class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j=0,len(nums)
        m=len(nums)
        while(m):
            index = (i+j)//2
            print(i,j,index)
            if nums[index]==target:
                return index
            elif nums[index]>target:
                j = index
            else:
                i = index
            m//=2
        return -1