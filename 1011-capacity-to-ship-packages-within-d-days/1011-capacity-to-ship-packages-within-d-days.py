class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = 1,sum(weights)
        ans = high
        while(low<=high):
            mid = (low+high)//2
        
            if self.dayReq(weights,mid)>days:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        
        return ans
    
    def dayReq(self,weights,capacity):
        total = 1
        curr = 0
        for weight in weights:
            if weight>capacity:
                return 2**32
            elif curr+weight<capacity:
                curr+=weight
            else:
                total+=1
                curr=weight
        return total
