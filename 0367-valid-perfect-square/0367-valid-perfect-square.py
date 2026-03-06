class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        low,high=0,num//2
        while(low<=high):
            mid = (low+high)//2
            mid_sq = mid*mid

            if mid_sq==num:
                return True
            elif mid_sq<num:
                low = mid+1
            else:
                high = mid-1

        return False