class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        length = len(nums)
        recall = {}
        for i in range(1,length):
            nums[i]+=nums[i-1]

        for num in nums:
            if num==k:
                count+=1
            if num-k in recall:
                count+=recall[num-k]

            recall[num]=recall.get(num,0)+1
        
        return count


                