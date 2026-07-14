class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        res = []

        for i in range(l-3):
            if i+3<l and nums[i] + nums[i+1] + nums[i+2] + nums[i+3]>target:
                return res
            if i!=0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,l-2):
                if j+2<l and nums[i]+nums[j] + nums[j+1] + nums[j+2]>target:
                    break
                if (j-1>i and nums[j-1]==nums[j]):
                    continue
                
                start,end = j+1,l-1
                while(start<end):
                    total = nums[i] + nums[j] + nums[start] + nums[end]

                    if total == target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        
                        while(start+1<l and nums[start]==nums[start+1]):
                            start+=1
                        while(end>0 and nums[end]==nums[end-1]):
                            end-=1
                        start+=1
                        end-=1

                    elif total > target:
                        while(end>0 and nums[end]==nums[end-1]):
                            end-=1
                        end-=1
                    else:
                        while(start+1<l and nums[start]==nums[start+1]):
                            start+=1
                        start+=1

        return res