class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = len(nums)
        memo = [0]*(l+1)
        for num in nums:
            if num>l:
                memo[l]+=1
            else:
                memo[num]+=1
        
        for i in range(l-1,-1,-1):
            memo[i]+=memo[i+1]
        
        for i in range(l+1):
            if i==memo[i]:
                return i
        return -1