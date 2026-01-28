class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        length = len(nums)
        recall = {}
        for num in range(1,length):
            nums[num]+=nums[num-1]

        for num in nums:
            if num==k:
                count+=1
            if num-k in recall:
                count+=recall[num-k]

            if num not in recall:
                recall[num]=1
            else:
                recall[num]+=1
        
        return count


                