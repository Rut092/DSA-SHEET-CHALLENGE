import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_mapping = Counter(nums)
        h = [[-freq_mapping[i],i] for i in freq_mapping]
        heapq.heapify(h)
        res = []
        for i in range(k):
            _ ,key = heapq.heappop(h)
            res.append(key)
        return res