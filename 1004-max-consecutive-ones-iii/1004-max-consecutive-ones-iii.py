class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flip = i = 0
        for j in range(len(nums)):
            if nums[j]==0:
                flip+=1

            if flip>k:
                if nums[i]==0:
                    flip-=1
                i+=1 

        return j-i+1