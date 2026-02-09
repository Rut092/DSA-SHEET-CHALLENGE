class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    
        row,col=len(grid),len(grid[0])
        total = 0
        res = None
        n = row*col
        tot_sum = n*(n+1)//2

        for i in range(row):
            for j in range(col):
                num = abs(grid[i][j])
                total+=num
                a = ((num-1)//row)
                b = ((num-1)%col)
                grid[a][b]=-grid[a][b]
                if grid[a][b]>0:
                    res = abs(grid[i][j])
    
        return [res,tot_sum-(total-res)]
        