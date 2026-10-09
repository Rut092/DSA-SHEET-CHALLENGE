class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        mapping = {}
        max_count = 0
        i = j = 0
        count = 0
        for j in range(l):
            if s[j] in mapping and mapping[s[j]]>=i:
                i = mapping[s[j]]+1

            mapping[s[j]]= j
            max_count = max(max_count,j-i+1)

        return max_count
        