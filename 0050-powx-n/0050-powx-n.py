class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0: 
            x = 1/x
            n = -n

        return self.calcIter(x,n)

    def calcRec(self,x,n):
        if n==0:
            return 1
        curr = self.calcRec(x,n//2)
        if n%2==0: return curr*curr
        else: return curr*curr*x

    def calcIter(self,x,n):
        
        val = 1
        while(n):
            if n%2==1:
                val = val*x
                n-=1
            x*=x
            n//=2
        return val


        