class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = j = 0
        length = len(nums)
        while(j<length and i<length):
            if nums[j]>0:
                if nums[i]<0:
                    nums[i],nums[j] = nums[j],nums[i]
                i+=2
            j+=1
        return nums  