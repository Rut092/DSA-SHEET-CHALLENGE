import heapq
from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        freq_map = Counter(hand)
        h = [i for i in freq_map]
        heapq.heapify(h)

        while(h):
            ele = h[0]
            if ele in freq_map:
                for i in range(ele,ele+groupSize):
                    if i not in freq_map:
                        return False
                    freq_map[i]-=1
                    if freq_map[i]==0:
                        del freq_map[i] 
            else:
                heapq.heappop(h)
        return True