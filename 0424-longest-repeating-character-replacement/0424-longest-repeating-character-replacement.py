import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        freq_map = collections.defaultdict(int)
        maxi = i = 0

        for j in range(l):
            
            freq_map[s[j]]+=1
            maxi = max(maxi,freq_map[s[j]])

            if j-i+1 - maxi > k:
                freq_map[s[i]]-=1
                i+=1

        return j-i+1