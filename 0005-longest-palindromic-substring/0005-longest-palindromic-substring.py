class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        low,high=0,0
        for i in range(l):
            for mini,maxi in [[i,i],[i,i+1]]:
                while(mini>=0 and maxi<l):
                    if s[maxi]!=s[mini]:
                        break
                    if high-low<maxi-mini:
                        high,low = maxi,mini
                    
                    maxi+=1
                    mini-=1
        
        return s[low:high+1]