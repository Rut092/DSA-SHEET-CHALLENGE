class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r_str=""
        opened = 0
        for i in s:
            if i=='(':
                if opened>0:
                    r_str+=i
                opened+=1
            else:
                if opened>1:    
                    r_str+=i
                opened-=1
        
        return r_str