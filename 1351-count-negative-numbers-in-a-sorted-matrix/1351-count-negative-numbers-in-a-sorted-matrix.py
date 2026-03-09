class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        rows,cols = len(grid),len(grid[0])
        for i in range(rows):
            low,high = 0,cols-1
            ans = cols
            while(low<=high):
                mid = (low+high)//2
                if grid[i][mid]<0:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
                    
            total+=(cols-ans)

        return total