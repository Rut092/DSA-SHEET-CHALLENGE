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
            
            for i in range(idx+1,l+1):
                if num[idx] == '0' and i > idx + 1:
                    break
                new_num = int(num[idx:i])
                if idx==0:
                    calc(i,[num[idx:i]],int(num[idx:i]),int(num[idx:i]))
                else:
                    calc(i,exp+['+',str(new_num)],new_num,value+new_num)
                    calc(i,exp+['-',str(new_num)],-new_num,value-new_num)
                    calc(i,exp+['*',str(new_num)],prev_val*new_num,value-prev_val+prev_val*new_num)

        calc(0,[],0,0)
        return res

            