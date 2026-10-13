class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        l = len(nums)

        def nOdd(n):
            count = total = 0
            i = 0

            for j in range(l):
                if nums[j]%2==1:
                    count+=1

                while(count>n):
                    if nums[i]%2==1:
                        count-=1
                    i+=1
                
                total+=(j-i+1)

            return total
        
        return nOdd(k)-(nOdd(k-1) if k-1>=0 else 0)