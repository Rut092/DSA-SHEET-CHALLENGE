class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        low,high = 1,max(bloomDay)
        ans = -1
        while(low<=high):
            mid = (low+high)>>1
            getVal = self.findDays(mid,m,k,bloomDay)

            if getVal == True:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans
    
    def findDays(self,days,m,k,bloomDay):
        boq = 0
        flower = k
        for i in bloomDay:
            if i<=days:
                flower-=1
                if flower==0:
                    boq+=1
                    flower = k
            else:
                flower = k
        return True if boq>=m else False
