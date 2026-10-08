class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        res = []
        i,j = intervals[0]

        for a,b in intervals:
            if a<=i:
                i=a

            if a<=j:
                j=max(j,b)
            
            else:
                res.append([i,j])
                i,j=a,b
        res.append([i,j])
        return res        