class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n==1:
            return 5

        def pow(num):
            print(num)
            if num==1:
                return 20
            elif num%2==0:
                val = pow(num//2)
                return (val*val)% MOD
            else:
                return (20*pow(num-1))%MOD
        
        val = pow(n//2)
        
        if n%2==0:
            return val
        else:
            return (val*5)%MOD
        