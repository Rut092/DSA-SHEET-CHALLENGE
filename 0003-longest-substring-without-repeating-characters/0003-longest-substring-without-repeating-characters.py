class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        l = len(s)
        start,end = 0,0
        total = 0
        while(end<l):
            if s[end] in map and start!=end:
                map.remove(s[start])
                start+=1
            else:
                map.add(s[end])
                total = max(total,end-start+1)
                end+=1

        return total