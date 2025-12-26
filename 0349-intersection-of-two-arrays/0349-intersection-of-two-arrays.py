class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = {}
        ans = []
        for i in nums1:
            a[i]=1
        for i in nums2:
            if a.get(i,0):
                a[i]-=1
                ans.append(i)
        return ans
        
        