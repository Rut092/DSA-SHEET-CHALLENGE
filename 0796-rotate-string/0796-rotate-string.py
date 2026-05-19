class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l = len(s)
        if l!= len(goal):
            return False
        heystack = goal+goal
        lps = [0]*l
        prevLPS,i=0,1
        while(i<l):
            if s[i]==s[prevLPS]:
                lps[i]=prevLPS+1
                i+=1
                prevLPS+=1
            elif prevLPS==0:
                lps[i]=0
                i+=1
            else:
                prevLPS = lps[prevLPS-1]
        
        i = j = 0
        while(i<len(heystack)):
            if heystack[i]==s[j]:
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j = lps[j-1]
    
            if j>=l:
                return True

        return False