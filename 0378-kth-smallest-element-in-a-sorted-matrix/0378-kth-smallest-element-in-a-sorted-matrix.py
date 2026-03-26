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

            if count>=k:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans

    def countKth(self,matrix,mid,n):
        count = 0
        row,col = 0,n-1
        while(row<n and col>=0):
            if matrix[row][col]<=mid:
                count+=(col+1)
                row+=1
            else:
                col-=1

        return count
        # for row in matrix:
        #     low,high = 0,n-1
        #     while(low<=high):
        #         mid = (low+high)//2

        #         if row[mid]<=k:
        #             low = mid+1
        #         else:
        #             high = mid-1
        #     ans+=(high+1)

        return ans