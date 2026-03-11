class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        l=len(piles)
        ans=high
        while(low<=high):
            speed = (low+high)//2

            value = 0
            for pile in piles:
                value+=(pile//speed)
                if pile%speed>0:
                    value+=1
                    
            if value==h:
                return speed
            elif value>h:
                low = speed+1
            else:
                ans = speed
                high = speed-1
            
        return ans



        


