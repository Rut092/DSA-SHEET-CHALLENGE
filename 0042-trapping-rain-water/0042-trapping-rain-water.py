class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = len(height)
        mini = self.miniH(height,l)

        for i in range(l):
            total+= (mini[i] - height[i])
        return total


    def miniH(self,height,l):
        arr = [height[0]]
        for i in range(1,l):
            arr.append(max(height[i],arr[-1]))

        maxi = height[-1]
        for i in range(l-1,-1,-1):
            maxi = max(maxi,height[i])
            arr[i] = min(arr[i],maxi)
        
        return arr