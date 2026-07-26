class Solution(object):
    def findPeakGrid(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        row,col = len(matrix),len(matrix[0])
        low,high= 0,col-1
        while(low<=high):
            mid = (low+high)>>1
            
            max_ele_ind = 0
            for i in range(row):
                if matrix[i][mid]>matrix[max_ele_ind][mid]:
                    max_ele_ind = i
          
            if mid-1>=0 and matrix[max_ele_ind][mid-1]>matrix[max_ele_ind][mid]:
                high = mid-1
            elif mid+1<col and matrix[max_ele_ind][mid+1]>matrix[max_ele_ind][mid]:
                low = mid+1
            else:
                return [max_ele_ind,mid]
        
        return [-1,-1]