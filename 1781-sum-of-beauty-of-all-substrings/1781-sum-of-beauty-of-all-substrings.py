class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        count = 0

        for i in range(l):
            book = {}
            for j in range(i,l):
                maxi,mini= 0,float('inf')
                if not s[j] in book:
                    book[s[j]]=1
                else:
                    book[s[j]]+=1

                for k in book:
                    if book[k]<mini: mini=book[k]
                    if book[k]>maxi: maxi=book[k]

                count+=maxi-mini
                
        return count