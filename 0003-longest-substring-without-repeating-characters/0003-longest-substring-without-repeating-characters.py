class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = len(s)
        start,end = 0,0
        total = 0
        while(end<l):
            if s[end] in map and map[s[end]]>=start:
                start = map[s[end]]+1
            else:
                map[s[end]]=end
                total = max(total,end-start+1)
                end+=1

        return total