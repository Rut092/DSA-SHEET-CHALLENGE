class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def binFind(start,end,isFirst):
            curr = -1
            while(start<=end):
                mid = (start+end)>>1
                if nums[mid]==target:
                    curr = mid
                    if isFirst:
                        end = mid-1
                    else:
                        start = mid+1

                elif nums[mid]>target:
                    end = mid-1
                else:
                    start = mid+1

            return curr

        return [binFind(0,len(nums)-1,True),binFind(0,len(nums)-1,False)]