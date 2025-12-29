class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        def findIndex(small):
            i,j=0,len(nums)-1
            found = -1
            while(i<=j):
                index = (i+j)//2
                if nums[index]==target:
                    if small:
                        if found!=-1:
                            found = min(found,index)
                        else:
                            found = index
                        j=index-1
                    else:
                        found = max(found,index)
                        i=index+1
                elif nums[index]>target:
                    j = index-1
                else:
                    i = index+1
            return found
        return [findIndex(True),findIndex(False)]