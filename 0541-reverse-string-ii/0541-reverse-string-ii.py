class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr = [i for i in s]
        l= len(s)
        for i in range(0,l,2*k):
            a,b=i,min(l-1,i+k-1)
            while(a<b):
                arr[a],arr[b]=arr[b],arr[a]
                a,b=a+1,b-1
        return "".join(arr)
            