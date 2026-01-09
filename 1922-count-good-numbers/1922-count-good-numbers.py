class Solution:
    def countGoodNumbers(self, n: int) -> int:
        count=1
        num = 20
        seq = n//2
        while(seq):
            if seq%2==0:
                num= (num*num)%(10**9+7)
                seq//=2
            else:
                count= (count*num)%(10**9+7)
                seq-=1
        return count%(10**9+7) if n%2==0 else count*5%(10**9+7)