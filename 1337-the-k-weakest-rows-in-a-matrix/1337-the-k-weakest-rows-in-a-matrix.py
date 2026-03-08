import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        res = []
        length = len(mat[0])-1

        def findInd(arr,l):
            low,high=0,l
            ans = -1
            while(high>=low):
                mid = (low+high)//2
                if arr[mid]==1:
                    ans=mid
                    low = mid+1
                else:
                    high=mid-1

            return ans

        for i in range(len(mat)):
            heapq.heappush(heap,[findInd(mat[i],length),i])
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
