class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        stack = []
        for i in s:
            if len(stack)==0 and i=='(':
                stack.append(i)
            elif i=='(':
                stack.append(i)
                arr.append(i)
            elif i==')' and len(stack)==1 and stack[-1]=='(':
                stack.pop()
            else:
                arr.append(i)
                stack.pop()
        
        return "".join(arr)