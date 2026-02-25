class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        heystack = goal + goal 
        l = len(s)
        l_h = len(heystack)
        if l+l!=l_h: return False
        lps = [0]*l
        prevLPS,i=0,1
        while(i<l):
            if s[i]==s[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS+=1
                i+=1
            elif prevLPS==0:
                lps[i]=0
                i+=1
            else:
                prevLPS = lps[prevLPS-1]
            
        i,j=0,0
        while(i<l_h):
            if s[j]==heystack[i]:
                i+=1
                j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]

            if l==j: return True
        return False



