class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for idx in range(len(nums)):
            curr_ele = nums[idx]
            low,high = 0,len(res)-1
            while(low<=high):
                mid = (low+high)//2
                if res[mid]==nums[idx]:
                    low=mid
                    break
                elif res[mid]>nums[idx]:
                    high = mid-1
                else:
                    low = mid+1
            
            if low<len(res):
                res[low]=curr_ele
            else:
                res.append(curr_ele)

        return len(res)


        