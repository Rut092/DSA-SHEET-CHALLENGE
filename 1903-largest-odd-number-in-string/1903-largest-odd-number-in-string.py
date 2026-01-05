class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = int(num)
        while(num and num%2==0):
            num//=10
        return "" if num==0 else str(num)