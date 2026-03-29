class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        low,high=0,0
        for i in range(l):
            mini,maxi=i,i
            while(mini>=0 and maxi<l):
                if s[maxi]==s[mini]:
                    if high-low<maxi-mini:
                        high,low = maxi,mini
                else:
                    break
                maxi+=1
                mini-=1

            mini,maxi=i,i+1
            while(mini>=0 and maxi<l):
                if s[maxi]==s[mini]:
                    if high-low<maxi-mini:
                        high,low = maxi,mini
                else:
                    break
                maxi+=1
                mini-=1
        
        return s[low:high+1]