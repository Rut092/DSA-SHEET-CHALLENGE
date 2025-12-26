class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [i for i in s]
        vovel = ['a','e','i','o','u']
        i,j=0,len(s)-1
        l = len(s)

        while(i<j):
            while(i<l and s[i].lower() not in vovel):
                i+=1
            while(j>=0 and s[j].lower() not in vovel):
                j-=1
            if i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1

        return "".join(s)
        
        