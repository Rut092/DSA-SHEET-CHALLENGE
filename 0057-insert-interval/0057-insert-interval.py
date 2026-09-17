class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        res = []
        i = 0
        n = len(intervals)
        a,b = newInterval

        while(i<n and intervals[i][0]<a and intervals[i][1]<a):
            res.append(intervals[i])
            i+=1
        
        while(i<n and intervals[i][0]<=b):
            
            a = min(a,intervals[i][0])
            b = max(b,intervals[i][1])
            i+=1
    
        res.append([a,b])

        while(i<n and intervals[i][0]>b):
            res.append(intervals[i])
            i+=1

        
        return res