class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        idx = 0
        INT_MAX,INT_MIN = 2**31-1,-2**31

        if not s:
            return 0
        if s[0]=='-':
            sign = -1
            idx+=1
        if s[0]=='+':
            sign = 1
            idx+=1

        def calculate(idx,curr_res):
            if idx>=len(s) or not s[idx].isdigit():
                return curr_res*sign
            
            curr_res = 10*curr_res + int(s[idx])

            if sign==1 and curr_res>INT_MAX:
                return INT_MAX

            elif sign==-1 and -curr_res<INT_MIN:
                return INT_MIN

            return calculate(idx+1,curr_res)


        return calculate(idx,0)
            