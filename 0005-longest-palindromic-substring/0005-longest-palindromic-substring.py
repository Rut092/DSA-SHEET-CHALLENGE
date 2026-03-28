class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        output =[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                low,high=i,j
                isTrue = True
                if j-i+1<=len(output):
                    continue
                while(low<=high):
                    if s[low]!=s[high]:
                        isTrue = False
                        break
                    low+=1
                    high-=1
                if isTrue and j-i+1>len(output):
                    output = s[i:j+1]

        return output