class Solution:
    def reverse(self, x: int) -> int:
        # solution
        rev,i,num = 0,0,abs(x)
        while(num):
            rev= rev*10+ num%10
            num=num//10
            i+=1
            if rev>2**31-1:
                return 0
        return rev if x>0 else -rev