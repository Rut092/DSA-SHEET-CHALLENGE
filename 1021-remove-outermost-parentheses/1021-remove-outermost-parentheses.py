class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        opened = 0
        for i in s:
            if i=='(':
                if opened>0:
                    arr.append(i)
                opened+=1
            else:
                if opened>1:    
                    arr.append(i)
                opened-=1
        
        return "".join(arr)