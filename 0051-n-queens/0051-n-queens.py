class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        dp = [["."]*n for _ in range(n)]
        res = []
        rows,diag1,diag2 = set(),set(),set()

        def calc(idx):
            if idx==n:
                res.append(["".join(string) for string in dp])
                return

            for i in range(n):

                if i in rows:
                    continue
                if i-idx in diag1:
                    continue
                if i+idx in diag2:
                    continue

                dp[i][idx] = 'Q'
                rows.add(i)
                diag1.add(i - idx)
                diag2.add(i + idx)

                calc(idx+1)
                
                dp[i][idx] = '.'
                rows.remove(i)
                diag1.remove(i - idx)
                diag2.remove(i + idx)
                

        calc(0)
        return res



        
