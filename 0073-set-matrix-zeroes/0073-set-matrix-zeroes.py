class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        h = len(matrix)
        v = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(h):
            for j in range(v):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            for j in range(v):
                matrix[i][j]=0
        for j in cols:
            for i in range(h):
                matrix[i][j]=0

        