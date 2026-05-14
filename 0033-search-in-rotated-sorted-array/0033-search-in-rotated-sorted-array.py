class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end = 0,len(nums)-1
        while(start<=end):
            mid = (start+end)>>1
            if nums[mid]==target:
                return mid
            elif nums[start]<=nums[mid]:
                if nums[start]<=target<=nums[mid]:
                    end = mid
                else:
                    start = mid+1
            else:
                if nums[mid]<=target<=nums[end]:
                    start = mid
                else:
                    end = mid-1
                
        return -1