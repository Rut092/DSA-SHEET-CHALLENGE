class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat),len(mat[0])
        for row in range(rows):
            low,high = 0,cols-1
            while(low<high):
                col = (low+high)>>1
    
                if mat[row][col]<mat[row][col+1]:
                    low = col+1
                else:
                    high = col
            
            top = bottom = True

            if row-1>=0 and mat[row-1][high]>mat[row][high]: top=False
            if row+1<rows and mat[row+1][high]>mat[row][high]:bottom=False

            if top and bottom: return [row,high]