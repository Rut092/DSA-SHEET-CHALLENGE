class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low,high = matrix[0][0],matrix[-1][-1]
        n = len(matrix)
        ans = high
        while(low<=high):
            mid = (low+high)//2
            count = self.countKth(matrix,mid,n)
            print(mid,count)

            if count>=k:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans
        
    def countKth(self,matrix,k,n):
        ans = 0
        for row in matrix:
            low,high = 0,n-1
            while(low<=high):
                mid = (low+high)//2

                if row[mid]<=k:
                    low = mid+1
                else:
                    high = mid-1
            ans+=(high+1)

        return ans