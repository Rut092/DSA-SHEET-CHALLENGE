class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0] 
        count = 0
        for i in nums:
            if i==ele:
                count+=1
            elif count==1:
                ele = i
                count = 1
            else:
                count-=1

        return ele