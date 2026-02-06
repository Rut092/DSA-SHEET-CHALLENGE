class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start,end=intervals[0]
        for i in range(1,len(intervals)):
            t_start,t_end = intervals[i]

            if t_start<=end:
                end = max(end,t_end)
            else:
                res.append([start,end])
                start,end=t_start,t_end
        res.append([start,end])
        return res