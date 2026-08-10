class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def calculate(opened,closed,val):
            if opened==n and closed==n:
                res.append("".join(val))
                return 
            
            if opened<n:
                calculate(opened+1,closed,val+['('])

            if opened>closed:
                calculate(opened,closed+1,val+[')'])
            
        calculate(0,0,[])
        return res