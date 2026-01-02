class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        maxi,ind=0,0
        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            count=0
            for col in range(cols):
                count+=mat[row][col]
            if count>maxi:
                maxi,ind=count,row
        return [ind,maxi]