class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        g_len,s_len = len(g),len(s)

        while(i<g_len and j<s_len):
            if g[i]<=s[j]:
                i+=1
            j+=1
        
        return i