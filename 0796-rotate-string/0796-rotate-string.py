class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        break_pt = -1
        s_len = len(s)
        
        if s_len!=len(goal):
            return False

        i = j = 0
        while(i<s_len and j<s_len):
            if s[i]!=goal[j]:
                i=0
                j+=1
                break_pt=-1
            else:
                if break_pt==-1:
                    break_pt=j
                i+=1
                j+=1

        return False if break_pt==-1 else s==goal[break_pt:]+goal[:break_pt]