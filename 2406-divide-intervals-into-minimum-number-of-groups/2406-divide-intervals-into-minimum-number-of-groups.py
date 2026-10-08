class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        l = len(intervals)
        start,end = [],[]
        for i,j in intervals:
            start.append(i)
            end.append(j)

        start.sort()
        end.sort()

        i,j=0,0
        res = 0
        group = 0
        while(i<l):
            if start[i]<=end[j]:
                i+=1
                group+=1
            else:
                j+=1
                group-=1
            res = max(res,group)
        
        return res
