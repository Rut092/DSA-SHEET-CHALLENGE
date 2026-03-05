class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        res=[]
        for a in range(l-3):
            if nums[a]+nums[a+1]+nums[a+2]+nums[a+3]>target:
                break
            if a>0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1,l-2):
                if b-1>a and nums[b]==nums[b-1]:
                    continue
                c=b+1
                d=l-1

                while(c<d):
                    total = nums[a]+nums[b]+nums[c]+nums[d]
                    if total==target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        while(c<d and nums[c]==nums[c+1]):
                            c+=1
                        c+=1
                        while(c<d and nums[d]==nums[d-1]):
                            d-=1
                        d-=1
                    elif total<target:
                        c+=1
                    else:
                        d-=1
        
        return res