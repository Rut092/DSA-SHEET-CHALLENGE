class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        length = len(height)
        l_max = r_max = l = 0
        r = length-1
        while(l<r):
            if height[l]<=height[r]:
                if l_max>height[l]:
                    count+= (l_max-height[l])
                else:
                    l_max = height[l]
                l+=1
            else:
                if r_max>height[r]:
                    count+=(r_max-height[r])
                else:
                    r_max = height[r]
                r-=1
        
        return count