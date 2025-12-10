class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0) :
            return False
        rev_int = 0

        while(x>rev_int):
            rev_int,x = x%10 + rev_int*10,x//10

        return (x==rev_int) or (x==rev_int//10)

        