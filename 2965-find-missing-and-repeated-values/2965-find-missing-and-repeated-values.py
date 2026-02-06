class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    
        row,col=len(grid),len(grid[0])
        total = (row*col*(row*col+1))//2
        res = 0
        book={}
        found = None
        for i in range(row):
            for j in range(col):
                res+=grid[i][j]
                if grid[i][j] in book:
                    found = grid[i][j]
                else:
                    book[grid[i][j]]=1

        return [found,abs(total-res+found)]