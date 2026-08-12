class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        book = { '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l = len(digits)
        output = []

        def calc(idx,op):
            if l==idx:
                output.append("".join(op[:]))
                return 

            for letter in book[digits[idx]]:
                op.append(letter)
                calc(idx+1,op)
                op.pop()
        
        calc(0,[])
        return output    
        