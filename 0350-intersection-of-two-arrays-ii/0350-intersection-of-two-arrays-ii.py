class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        hash_set = {}
        for i in nums1:
            hash_set[i]= hash_set.get(i,0)+1
        for i in nums2:
            if hash_set.get(i,-1)>0:
                ans.append(i)
                hash_set[i]-=1
        return ans