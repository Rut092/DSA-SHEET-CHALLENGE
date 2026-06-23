class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        l = len(nums)
        for i in range(l-2):
            if nums[i]>0 or nums[i]+nums[i+1]+nums[i+2]>0:
                break

            if i>0 and nums[i-1]==nums[i]:
                continue

            j,k=i+1,l-1
            while(j<k):
                temp = nums[i]+nums[j]+nums[k]
                if temp==0:
                    res.append([nums[i],nums[j],nums[k]])
                    
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    k-=1
                elif temp>0:
                    k-=1
                else:
                    j+=1

        return res