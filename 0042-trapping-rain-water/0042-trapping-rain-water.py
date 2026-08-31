class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = len(height)
        pMax = self.pMax(height,l)
        sMax = self.sMax(height,l)

        for i in range(l):
            total+= (min(pMax[i],sMax[i]) - height[i])
        
        return total


    def pMax(self,height,l):
        arr = [height[0]]
        for i in range(1,l):
            arr.append(max(height[i],arr[-1]))
        return arr
    
    def sMax(self,height,l):
        arr = [height[-1]]
        for i in range(l-2,-1,-1):
            arr.append(max(height[i],arr[-1]))
        return arr[::-1]