class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
            
        l1,l2 = len(nums1),len(nums2)
        low,high = 0,l1
        l = l1+l2
        left = (l+1)//2

        while(low<=high):
            mid1 = (low+high)>>1
            mid2 = left-mid1
            a1 = a2 = float('-inf')
            x1 = x2 = float('inf')

            if mid1<l1: x1 = nums1[mid1]
            if mid2<l2: x2 = nums2[mid2]
            if mid1-1>=0: a1 = nums1[mid1-1]
            if mid2-1>=0: a2 = nums2[mid2-1]

            if a1>x2:
                high = mid1-1
            elif a2>x1:
                low = mid1+1
            else:
                if l%2!=0:
                    return max(a1,a2)
                return (max(a1,a2)+min(x1,x2))/2


        return 0