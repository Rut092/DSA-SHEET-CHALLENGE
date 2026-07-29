class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count,l = 0,len(s)
        for i in range(l):
            book = {}
            for j in range(i,l):
                maxi,mini = 0,float('inf')
                if not s[j] in book:
                    book[s[j]] = 1
                else:
                    book[s[j]]+=1
                
                for k in book:
                    if book[k]>maxi: maxi = book[k]
                    if book[k]<mini: mini = book[k]

                count+=(maxi-mini)

        return count