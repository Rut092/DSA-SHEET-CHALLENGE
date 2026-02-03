class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        is_first_col = False
        
        for row in range(rows):
            if matrix[row][0]==0:
                is_first_col = True
            for col in range(1,cols):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    matrix[0][col]=0
                
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,0,-1):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0
            if is_first_col:
                matrix[row][0]=0





        