class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high = 0,n
        res = 0
        while(low<=high):
            mid = (low+high)//2
            count = (mid*(mid+1))//2
    
            if count==n:
                return mid
            elif count>n:
                high = mid-1
            else:
                res=mid
                low = mid+1
        return res