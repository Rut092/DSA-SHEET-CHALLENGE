class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        x,y=0,0
        row,col = len(mat),len(mat[0])
        while(True):
            left = right= top = bottom = True
            if x-1>=0 and mat[x-1][y]>mat[x][y]: top = False
            if x+1<row and mat[x+1][y]>mat[x][y]: bottom = False
            if y-1>=0 and mat[x][y-1]>mat[x][y]: left = False
            if y+1<col and mat[x][y+1]>mat[x][y]: right = False

            if left and right and top and bottom:
                return [x,y]

            if not bottom:
                x+=1
            elif not top:
                x-=1
            elif not right:
                y+=1
            elif not left:
                y-=1
        