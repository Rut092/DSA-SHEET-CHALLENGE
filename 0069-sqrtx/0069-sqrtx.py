class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low,high = 0,x//2
        ans=0
        while(low<=high):
            mid = (low+high)//2
            sq_term = mid*mid
            if sq_term==x:
                return mid
            elif sq_term<x:
                ans = mid
                low = mid+1
            else:
                high = mid-1

        return ans