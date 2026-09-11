import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)

        for i in range(k,len(nums)):
            ele = heapq.heappop(h)
            heapq.heappush(h,max(ele,nums[i]))
    
        return heapq.heappop(h)