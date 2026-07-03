class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = prefix_sum = 0
        recall = {0:1}

        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in recall:
                total+= recall[prefix_sum-k]
            recall[prefix_sum] = recall.get(prefix_sum,0)+1

        return total
