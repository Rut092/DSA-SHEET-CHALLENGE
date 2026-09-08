import collections
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = i = 0
            l = len(nums)
            freq_map = collections.defaultdict(int)
            for j in range(l):
                freq_map[nums[j]]+=1

                while len(freq_map)>k:
                    freq_map[nums[i]]-=1
                    if freq_map[nums[i]]==0:
                        del freq_map[nums[i]]
                    i+=1

                count+=(j-i+1)
                
            return count
        
        return atMost(k)-atMost(k-1)