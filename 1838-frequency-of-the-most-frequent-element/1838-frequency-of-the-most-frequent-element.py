class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        max_freq,i,j = 0,0,0
        nums = sorted(nums)
        sum = nums[i]
        while(j<len(nums) and i<=j):
            if nums[j]*(j-i+1)<=sum+k:
                max_freq=max(max_freq,j-i+1)
                j+=1
                if j<len(nums):
                    sum+=nums[j]
                else:
                    break
                
            else:
                sum-=nums[i]
                i+=1
    

        return max_freq
