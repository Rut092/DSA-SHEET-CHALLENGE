class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = m+n-1
        start,end = m-1,n-1
        while(start<total):
            if nums1[start]>nums2[end]:
                nums1[total]=nums1[start]
                start-=1
            else:
                nums1[total]=nums2[end]
                end-=1
            total-=1
        