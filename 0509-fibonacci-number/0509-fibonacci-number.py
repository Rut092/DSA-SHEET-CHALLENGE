class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        a,b=1,1
        for i in range(3,n+1):
            a,b=b,a+b
        return b        