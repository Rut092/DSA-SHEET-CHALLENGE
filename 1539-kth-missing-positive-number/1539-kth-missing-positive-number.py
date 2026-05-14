class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        start,end = 0,len(arr)-1
        while(start<=end):
            mid = (start+end)>>1
    
            if arr[mid]-(mid+1)<k:
                start = mid+1
            else:
                end = mid-1
        
        return start+k