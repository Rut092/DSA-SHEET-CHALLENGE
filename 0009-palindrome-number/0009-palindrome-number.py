class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = x
        rev = 0
        while(num):
            rev,num=rev*10 + num%10,num//10
            if rev==num:
                return True
        return True if x==rev else False