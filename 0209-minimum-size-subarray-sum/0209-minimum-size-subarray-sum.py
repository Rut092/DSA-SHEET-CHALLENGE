class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # l = len(nums)
        # curr_sum = left = 0
        # ans = float('inf')
        # for right in range(l):
        #     curr_sum+=nums[right]
        #     while(curr_sum>=target):
        #         ans = min(ans,right-left)
        #         curr_sum-=nums[left]
        #         left+=1
        
        # return ans+1 if ans!=float('inf') else 0
        l = len(nums)
        for i in range(1,l):
            nums[i]+=nums[i-1]
        nums = [0]+nums
        ans = float('inf')
        for i in range(l+1):
            find = target + nums[i]
            low,high = i+1,l
            while(low<=high):
                mid = (low+high)>>1
                if nums[mid]>=find:
                    ans = min(ans,mid-i)
                    high = mid-1
                else:
                    low = mid+1
            
        return ans if ans!=float('inf') else 0
