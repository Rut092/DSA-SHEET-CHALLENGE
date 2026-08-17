class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        value = start^goal
        count = 0
        while(value>0):
            count+=(value&1)
            value=value>>1
        return count