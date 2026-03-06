class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high = 0,n
        while(low<high):
            mid = (low+high)//2
            count = (mid*(mid+1))//2
            print(low,mid,high)
            if count==n:
                return mid
            elif count>n:
                high = mid-1
            elif ((mid+1)*(mid+2))//2>n:
                return mid
            else:
                low = mid+1
        return high