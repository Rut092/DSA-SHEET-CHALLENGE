class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        l1,l2 = len(arr1),len(arr2)
        count = 0

        def findRange(ele):
            low,high = 0,l2-1
            while(low<=high):
                mid = (low+high)//2
                if ele-d<=arr2[mid]<=ele+d:
                    return True
                elif ele-d>arr2[mid]:
                    low = mid+1
                else:
                    high = mid-1
 
            return False

        for i in range(l1):
            count+= 0 if findRange(arr1[i]) else 1
        
        return count
                
