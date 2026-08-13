class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        dp = [["."]*n for _ in range(n)]
        res = []

        def check_valid(queens):
            is_valid = True
            for i in range(len(queens)):
                for j in range(i+1,len(queens)):
                    a,b = queens[i]
                    c,d = queens[j]
                    if a==c or b==d or abs(a-c)==abs(b-d):
                        is_valid = False
            
            return is_valid


        def calc(idx,queens):
            if idx==n:
                res.append(["".join(string) for string in dp])
                return

            for i in range(n):
                dp[i][idx] = 'Q'
                queens.append([i,idx])
                if check_valid(queens):
                    calc(idx+1,queens)
                dp[i][idx] = '.'
                queens.pop()


        calc(0,[])
        return res



        
