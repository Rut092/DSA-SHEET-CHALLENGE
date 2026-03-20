class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows,cols = len(matrix),len(matrix[0])
        low,high = 0,rows*cols-1

        while(low<=high):
            mid = (low+high)//2
            row,col = (mid//cols),(mid%(cols))
            
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high = mid-1
            else:
                low = mid+1

        return False