class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_first_col = False

        cols,rows = len(matrix[0]),len(matrix)

        for i in range(rows):
            if matrix[i][0]==0:
                is_first_col = True
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[0][j] = matrix [i][0] = 0
        
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            
            if is_first_col == True:
                matrix[i][0]=0