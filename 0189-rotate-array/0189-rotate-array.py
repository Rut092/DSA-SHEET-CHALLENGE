import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i,j=0,l-1
        j=l-1
        while(i<j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        i,j=0,k%l-1
        while(i<j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        i,j=k%l,l-1
        while(i<j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        