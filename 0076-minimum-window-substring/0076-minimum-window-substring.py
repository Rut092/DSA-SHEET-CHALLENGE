import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq_map = collections.Counter(t)
        total_char = len(freq_map)
        matched = i = 0
        min_i,min_j=0,float('inf')

        for j in range(len(s)):
            if s[j] in freq_map:
                freq_map[s[j]]-=1
                if freq_map[s[j]]==0:
                    matched+=1

            while(matched==total_char):
                if min_j-min_i>j-i:
                    min_i,min_j=i,j
                
                if s[i] in freq_map:
                    freq_map[s[i]]+=1
                    if freq_map[s[i]]>0:
                        matched-=1
                
                i+=1

        return s[min_i:min_j+1] if min_j!=float('inf') else ""
            
