class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        i=0
        ans = ""
        while(num):
            ans+= (num//roman_map[i][0])*roman_map[i][1]
            num%=roman_map[i][0]
            i+=1
        return ans