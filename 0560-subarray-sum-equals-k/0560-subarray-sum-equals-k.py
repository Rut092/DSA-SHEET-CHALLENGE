class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        recall = {0:1}
        total = count = 0

        for num in nums:
            total+=num
            if total-k in recall:
                count+=recall[total-k]
            recall[total]=recall.get(total,0)+1
        
        return count


                