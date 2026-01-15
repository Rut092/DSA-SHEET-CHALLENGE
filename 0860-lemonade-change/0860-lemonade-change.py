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
                if cash[2]==0:
                    return False
                cash[2]-=1
                cash[1]+=1
            else:

                money-=5
                cash[0]+=1
                if cash[1]:
                    money-=10
                    cash[1]-=1
                if money//5<=cash[2]:
                    cash[2]-=money//5
                else:
                    return False

        return True