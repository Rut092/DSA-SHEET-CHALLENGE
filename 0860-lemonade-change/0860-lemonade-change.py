class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash = [0,0,0]
        for money in bills:
            if money==5:
                cash[2]+=1
            elif money==10:
                if not cash[2]:
                    return False
                cash[2]-=1
                cash[1]+=1
            else:
                if cash[1] and cash[2]:
                    cash[1]-=1
                    cash[2]-=1
                elif cash[2]>=3:
                    cash[2]-=3
                else:
                    return False

        return True