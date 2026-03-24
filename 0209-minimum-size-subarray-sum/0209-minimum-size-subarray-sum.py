class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # l = len(nums)
        # left = current_sum = 0
        # ans = float('inf')
        # for right in range(l):
        #     current_sum+= nums[right]
        #     while(current_sum>=target):
        #         ans = min(ans,right-left+1)
        #         current_sum-=nums[left]
        #         left+=1

        # return ans if ans!=float('inf') else 0


        l = len(nums)
        for i in range(1,l):
            nums[i]+=nums[i-1]

        nums = [0]+nums

        print(nums)
        ans = float('inf')
        
        for i in range(l+1):
            need = nums[i]+target
            low,high = i+1,l

            while(low<=high):
                mid = (low+high)//2
                if nums[mid]>=need:
                    ans = min(ans,mid-i)
                    high = mid-1
                else:
                    low = mid+1

        return ans if ans!= float('inf') else 0