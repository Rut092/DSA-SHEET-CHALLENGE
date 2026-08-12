class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        l = len(s)
        def calc(ind,op):
            if ind==l:
                res.append(op[:])
                return 
            for i in range(ind,l):
                low = ind
                high = i
                is_palindrome = True
                while(low<=high):
                    if s[low]!=s[high]:
                        is_palindrome = False
                        break
                    low+=1
                    high-=1
                
                if is_palindrome:
                    op.append(s[ind:i+1])
                    calc(i+1,op)
                    op.pop()
        calc(0,[])
        return res
    