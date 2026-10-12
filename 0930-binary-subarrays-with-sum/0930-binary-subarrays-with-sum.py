class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        l = len(nums)

        def atMost(k):
            i = total = curr_sum = 0
            for j in range(l):
                curr_sum+=nums[j]

                while(curr_sum>k):
                    curr_sum-=nums[i]
                    i+=1

                total+=(j-i+1)

            return total
        
        return atMost(goal)-(atMost(goal-1) if goal-1>=0 else 0)