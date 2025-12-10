class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num,rev= x,0
        while(num):
            rev,num=rev*10 + num%10,num//10
        return rev==x