class Solution:
    def mySqrt(self, x: int) -> int:
        prev=0
        curr=1
        while(curr>prev):
            curr_sq = curr*curr
            prev_sq = prev*prev
            
            if curr_sq==x:
                return curr
            elif curr_sq<x:
                prev = curr
                curr*=2
            else:
                curr=(prev+curr)//2

        return prev