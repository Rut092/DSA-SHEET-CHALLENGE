class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def count(prev,value):
            if len(prev)>=n:
                res.append(prev)
                return
            
            if value!=0:
                count(prev+"0",0)
            count(prev+'1',1)

        
        count("",-1)
        return res