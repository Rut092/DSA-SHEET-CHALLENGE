class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        total = i = 0
        flip = 0
        for j in range(len(nums)):
            if nums[j]==0:
                flip+=1

            while(flip>k):
                if nums[i]==0:
                    flip-=1
                i+=1 

            total = max(total,j-i+1)

        return total