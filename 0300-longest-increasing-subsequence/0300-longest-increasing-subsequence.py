class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        res = []
        for i in range(l):
            low = 0
            high=len(res)-1
            while(low<=high):
                mid = (low+high)//2

                if nums[i]==res[mid]:
                    low = mid
                    break
                elif res[mid]<nums[i]:
                    low = mid+1
                else:
                    high = mid-1
            
            if low<len(res): res[low] = nums[i]
            else: res.append(nums[i])

        print(res)
        return len(res)
                
