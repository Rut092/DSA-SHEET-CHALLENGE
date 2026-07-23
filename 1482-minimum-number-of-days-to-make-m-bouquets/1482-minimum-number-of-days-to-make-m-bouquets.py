class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        maxi = max(bloomDay)
        low,high = 1,maxi+1
        while(low<high):
            mid = (low+high)>>1
            getVal = self.findDays(mid,m,k,bloomDay)
            if getVal ==True:
                high = mid
            else:
                low = mid+1

        return high if high<maxi+1 else -1
    
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
