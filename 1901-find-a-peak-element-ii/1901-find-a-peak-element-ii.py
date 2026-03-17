class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat),len(mat[0])
        low,high = 0, cols-1
        while(low<=high):
            col = (low+high)//2
            max_row = 0
            for row in range(1,rows):
                if mat[row][col]>mat[max_row][col]:
                    max_row = row

            if col-1>=0 and mat[max_row][col]<=mat[max_row][col-1]:
                high = col-1
            elif col+1<cols and mat[max_row][col]<=mat[max_row][col+1]:
                low = col+1
            else:
                return [max_row,col]

        return []