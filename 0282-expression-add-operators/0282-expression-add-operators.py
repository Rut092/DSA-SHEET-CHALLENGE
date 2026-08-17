class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []   
        l = len(num)    
        def calc(idx,exp,prev_val,value):
            if idx==l: 
                if value==target:
                    res.append("".join(exp))
                return 
            curr_val = 0
            for i in range(idx,l):
                if num[idx] == '0' and i > idx:
                    break

                curr_val = curr_val*10 + int(num[i])
                part = num[idx:i+1]

                if idx==0:
                    exp.append(part)
                    calc(i+1,exp,curr_val,curr_val)
                    exp.pop()
                else:
                    exp.extend(['+',part])
                    calc(i+1,exp,curr_val,value+curr_val)
                    exp.pop()
                    exp.pop()

                    exp.extend(['-',part])
                    calc(i+1,exp,-curr_val,value-curr_val)
                    exp.pop()
                    exp.pop()

                    exp.extend(['*',part])
                    calc(i+1,exp,prev_val*curr_val,value-prev_val+(prev_val*curr_val))
                    exp.pop()
                    exp.pop()

        calc(0,[],0,0)
        return res

            