class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = len(nums2)
        for num in nums1:
            low,high = 0,l-1
            while(low<=high):
                mid = (low+high)//2
                if nums2[mid]==num:
                    return num
                elif nums2[mid]<num:
                    low = mid+1
                else:
                    high = mid-1
        return -1
        