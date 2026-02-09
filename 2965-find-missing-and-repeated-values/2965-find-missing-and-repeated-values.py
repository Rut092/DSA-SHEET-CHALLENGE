class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    
        row,col=len(grid),len(grid[0])
        total = 0
        for i in range(row):
            for j in range(col):
                num = abs(grid[i][j])
                total+=num
                a = ((num-1)//row)
                b = ((num-1)%col)
                grid[a][b]=-grid[a][b]

        ans = []
        for i in range(row):
            for j in range(col):
                if grid[i][j]>0:
                    ans.append(i*(row)+j+1)
        n = row*col
        tot_sum = n*(n+1)//2
        if tot_sum>total:
            return ans
        else:
            return ans[::-1]