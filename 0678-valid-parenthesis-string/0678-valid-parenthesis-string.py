class Solution:
    def checkValidString(self, s: str) -> bool:
        star,opened,closed = [],[],[]
        for i,char in enumerate(s):
            if char=='(':
                opened.append(i)
            elif char=='*':
                star.append(i)
            else:
                if opened:
                    opened.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while(star and opened):
            if opened[-1]>star[-1]:
                return False
            opened.pop()
            star.pop()
        return len(opened)==0