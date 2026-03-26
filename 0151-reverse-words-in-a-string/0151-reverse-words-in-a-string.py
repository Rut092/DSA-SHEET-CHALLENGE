class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        temp = ''
        l = len(s)
        start,end = 0,l-1

        for i in range(start,end+1):
            if s[i]==" ":
                if len(temp)>0:
                    res.append(temp)
                    temp =''
            else:
                temp+=s[i]
        
        if temp: res.append(temp)

        start,end = 0,len(res)-1
        while(start<end):
            res[start],res[end]=res[end],res[start]
            start+=1
            end-=1

        return " ".join(res)
