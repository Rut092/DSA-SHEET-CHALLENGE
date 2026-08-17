class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==divisor: return 1
        sign = True
        if dividend<0 and divisor>=0:
            sign = False
        if divisor<0 and dividend>=0:
            sign = False

        n,d= abs(dividend),abs(divisor)
        total = 0
        while(n>=d):
            count = 0
            while(n>=(d<<(count+1))):
                count+=1
            
            total+=(1<<count)
            n-=((d<<count))
        
        if total>=2**31 and sign: return 2**31-1
        if total>2**31 and not sign: return -2**31
        return total if sign else -total