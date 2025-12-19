import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        arr=[[0,l-1],[0,k%l-1],[k%l,l-1]]
        
        for x in arr:
            i,j=x
            while(i<j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

        