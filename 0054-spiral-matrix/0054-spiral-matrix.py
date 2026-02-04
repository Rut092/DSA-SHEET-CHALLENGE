class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),len(matrix[0])
        res = []
        i,j=0,0
        res.append(matrix[0][0])
        matrix[0][0]=-2**8
        while(True):
            while(j+1<cols and matrix[i][j+1]!=-2**8):
                res.append(matrix[i][j+1])
                matrix[i][j+1]=-2**8
                j+=1

            while(i+1<rows and matrix[i+1][j]!=-2**8):
                res.append(matrix[i+1][j])
                matrix[i+1][j]=-2**8
                i+=1
    
            while(j-1>=0 and matrix[i][j-1]!=-2**8):
                res.append(matrix[i][j-1])
                matrix[i][j-1]=-2**8
                j-=1
                
            while(i-1>=0 and matrix[i-1][j]!=-2**8):
                res.append(matrix[i-1][j])
                matrix[i-1][j]=-2**8
                i-=1
            if len(res)==rows*cols:
                break

        return res