class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low,high=0,num
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