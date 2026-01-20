class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            if carry==0:
                break
            digits[i]=(digits[i]+carry)%10
            carry = 1 if digits[i]==0 else 0
        return digits if carry==0 else [1]+digits

                