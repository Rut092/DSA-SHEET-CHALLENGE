class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_len,g_len = len(s),len(goal)

        if s_len!=g_len:
            return False

        for shift in range(s_len):
            match = True
            for index in range(s_len):
                if s[index]!=goal[(index+shift)%s_len]:
                    match=False
            if match==True:
                return True
        return False
        