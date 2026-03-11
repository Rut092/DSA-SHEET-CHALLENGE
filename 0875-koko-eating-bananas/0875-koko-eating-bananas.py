class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,l = 1,len(piles)
        high = ans = max(piles)
        while(low<=high):
            speed = (low+high)//2

            value = 0
            for pile in piles:
                value+=(pile//speed + int(pile%speed>0))
    
            if value>h:
                low = speed+1
            else:
                ans = speed
                high = speed-1
            
        return ans



        


