class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mod_str = ""
        for i in s:
            if 65<=ord(i)<=90:
                mod_str+=chr(ord(i)+32)
            elif 97<=ord(i)<=122:
                mod_str+=i
            elif 48<=ord(i)<=57:
                mod_str+=i
        i,j=0,len(mod_str)-1

        while(i<j):
            if mod_str[i]==mod_str[j]:
                i+=1
                j-=1
            else:
                return False
        return True