class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = len(bloomDay)
        low,high = 0,max(bloomDay)
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            count = self.total_boquets(mid,bloomDay,k)

            if count<m:
                low = mid+1
            else:
                ans = mid
                high = mid-1

        return ans

    def total_boquets(self,value,bloomDay,flowers):
        boquets_count = count_flower = 0

        for flo in bloomDay:
            if flo<=value:
                count_flower+=1
                if count_flower%flowers==0:
                    boquets_count+=1
                    count_flower=0
            else:
                count_flower=0

        return boquets_count
