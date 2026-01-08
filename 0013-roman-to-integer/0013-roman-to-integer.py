class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s_len = len(s)
        count=0
        for i in range(len(s)):
            if i+1==s_len:
                count+=values[s[i]]
            else:
                if values[s[i]]<values[s[i+1]]:
                    count-=values[s[i]]
                else:
                    count+=values[s[i]]

        return count
