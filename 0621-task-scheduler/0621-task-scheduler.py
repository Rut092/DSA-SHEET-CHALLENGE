from collections import deque,Counter
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        q = deque([])
        counter = Counter(tasks)
        h = [-x for x in counter.values()]
        heapq.heapify(h)
        total = 0
        curr_time = 0
        while(q or h):
            curr_time+=1

            if h:
                val = heapq.heappop(h)
                if val+1<0:
                    q.append([curr_time+n,val+1])

            if q and curr_time==q[0][0]:
                heapq.heappush(h,q.popleft()[1])
            
            total+=1

        return total