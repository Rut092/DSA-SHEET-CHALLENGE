class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n==1:
            return 5

        def pow(num):
            if num==0:
                return 1

            val = pow(num//2)

            if num%2==0:
                return (val*val)% MOD
            else:
                return (20*val*val)%MOD
        
        val = pow(n//2)
        if n%2==0:
            return val
        else:
            return (val*5)%MOD
        