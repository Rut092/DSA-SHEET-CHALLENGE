from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = len(s)
        freq_map = defaultdict(int)
        i = total = 0

        for j in range(l):
            freq_map[s[j]]+=1

            while(len(freq_map)>=3):
                total+=(l-j)

                freq_map[s[i]]-=1
                if freq_map[s[i]]==0:
                    del freq_map[s[i]]
                i+=1
                
        return total