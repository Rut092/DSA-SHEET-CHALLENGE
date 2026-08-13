class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        pal_memo = [[False]*l for _ in range(l)]

        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if s[i]==s[j]:
                    if j-i<=2 or pal_memo[i+1][j-1]:
                        pal_memo[i][j]= True

        memo = [-1]*(l+1)
        memo[l]= 0

        def calc(idx):
            if memo[idx]!=-1:
                return memo[idx]
    
            mini = float('inf')
            for i in range(idx,l):
                if pal_memo[idx][i]:
                    mini = min(mini,1 + calc(i+1))
                    if mini==1:
                        break
            
            memo[idx] = mini
            return mini

        return calc(0)-1