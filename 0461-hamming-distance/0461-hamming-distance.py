class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        value = x^y
        count = 0
        while(value>0):
            count+=(value&1)
            value=value>>1
        return count