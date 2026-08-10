class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def calculate(opened,closed,temp,val):
            if opened==n and closed==n:
                res.append("".join(val))
                return 
            
            if opened<n:
                calculate(opened+1,closed,temp+['('],val+['('])

            if opened>closed:
                if temp[-1]=='(':
                    temp.pop()
                    calculate(opened,closed+1,temp,val+[')'])
            
        calculate(0,0,[],[])
        return res