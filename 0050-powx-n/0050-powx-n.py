class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0:
            return 1
        x = x if n>0 else 1/x
        value = 1
        n= n if n>0 else -n
        
        while(n):
            if n%2==0:
                x*=x
                n//=2
            else:
                value*=x
                n-=1
        return value