class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = len(s)
        start  = total = 0
        for end in range(l):
            char = s[end]
            if char in map and map[char]>=start:
                start = map[char]+1
        
            map[char] = end
            total = max(total,end-start+1)

        return total