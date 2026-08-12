class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        l = len(s)
        dp = [False]*(l+1)
        dp[l]= True

        for i in range(l-1,-1,-1):
            for j in range(i+1,l+1):
                if s[i:j] in word_set and dp[j]:
                    dp[i] = True
                    break
            
        return dp[0]
