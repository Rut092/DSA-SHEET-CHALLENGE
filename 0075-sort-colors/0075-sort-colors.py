class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,k =0,0,len(nums)-1
        while(j<=k):
            if nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            elif nums[j]==2:
                if nums[k]!=2:
                    nums[j],nums[k]=nums[k],nums[j]
                k-=1
                j-=1

            j+=1

        # length = len(nums)
        # i=0
        # for j in range(length):
        #     if nums[j]==0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
        # for j in range(i,length):
        #     if nums[j]==1:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
                
