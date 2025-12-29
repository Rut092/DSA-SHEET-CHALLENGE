class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr = [i for i in s]
        l= len(s)
        m=0
        n=min(k-1,l-1)
        while(n<l and m<l):
            i,j=m,n
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            m+=2*k
            n=min(n+2*k,l-1)
        return "".join(arr)