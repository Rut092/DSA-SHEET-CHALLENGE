class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        opened = 0
        for i in s:
            if opened==0 and i=='(':
                opened+=1
            elif i=='(':
                opened+=1
                arr.append(i)
            elif i==')' and opened==1:
                opened-=1
            else:
                arr.append(i)
                opened-=1
        
        return "".join(arr)