class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        opened = 0
        for par in s:
            if par =='(':
                if opened>0:
                    arr.append('(')
                opened+=1
            else:
                if opened>1:
                    arr.append(')')
                opened-=1

        return "".join(arr)

