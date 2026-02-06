class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m+n-1
        i,j=m-1,n-1
        while(j>=0 and i>=0):
            if nums2[j]>nums1[i]:
                nums1[end]=nums2[j]
                j-=1
            else:
                nums1[end]=nums1[i]
                i-=1
            end-=1
        while(j>=0):
            nums1[end]=nums2[j]
            end-=1
            j-=1
        
        