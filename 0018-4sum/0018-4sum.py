class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res=[]
        # print(nums)
        for i in range(length-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,length-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                total = nums[i] + nums[j]
                
                k,l=j+1,length-1
                # print(i,j,k,l)
                while(k<l):
                    tot_sum = total+nums[k]+nums[l]
                    if tot_sum>target:
                        l-=1
                    elif tot_sum<target:
                        k+=1
                    else:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        while(k<l and nums[k]==nums[k+1]):
                            k+=1
                        while(k<l and nums[l]==nums[l-1]):
                            l-=1
                        k+=1
                        l-=1
        return res