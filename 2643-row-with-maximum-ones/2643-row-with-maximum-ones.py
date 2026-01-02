class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        maxi,ind=0,0
        for row in range(len(rows)):
            count=sum(mat[row])
            if count>maxi:
                maxi,ind=count,row
        return [ind,maxi]