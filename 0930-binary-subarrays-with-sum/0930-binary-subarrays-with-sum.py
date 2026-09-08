class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = len(nums)
        def atMost(k):
            count = i = 0
            total = 0
            for j in range(l):
                total+=nums[j]

                while total>k:
                    total-=nums[i]
                    i+=1

                count+=(j-i+1)
                
            return count
        
        return atMost(goal)- (atMost(goal-1) if goal-1>=0 else 0)