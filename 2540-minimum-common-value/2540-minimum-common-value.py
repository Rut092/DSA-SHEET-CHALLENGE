class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        l1,l2 = len(nums1),len(nums2)
        while(i<l1 and j<l2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return -1
        