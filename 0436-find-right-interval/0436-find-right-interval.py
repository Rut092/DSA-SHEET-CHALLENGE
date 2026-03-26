class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sorted_intervals = res = []
        l = len(intervals)

        for i in range(l):
            sorted_intervals.append([intervals[i][0],intervals[i][1],i])

        sorted_intervals.sort()

        for interval in intervals:
            low,high = 0,l-1
            ans = -1

            while(low<=high):
                mid = (low+high)//2 

                if sorted_intervals[0]<interval[1]:
                    low = mid+1
                else:
                    ans = sorted_intervals[2]
                    high = mid-1

            res.append(ans)

        return res