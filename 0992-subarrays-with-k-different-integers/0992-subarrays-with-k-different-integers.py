from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        l = len(nums)

        def nInt(n):
            i = total = 0
            mapping = defaultdict(int)

            for j in range(l):
                mapping[nums[j]]+=1

                while(len(mapping)>n):
                    mapping[nums[i]]-=1
                    if mapping[nums[i]]==0:
                        del mapping[nums[i]]
                    i+=1

                total+=(j-i+1)

            return total
        
        return nInt(k)-(nInt(k-1) if k-1>0 else 0)