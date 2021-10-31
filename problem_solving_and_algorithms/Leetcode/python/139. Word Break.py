class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [[False for i in range(len(s))] for x in range(len(s))]
        
        for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                
                if s[j : j + i] in wordDict:
                    dp[j][j + i - 1] = True
                else:
                    for k in range(j + 1, j + i):
                        if dp[j][k - 1] and dp[k][j + i - 1]:
                            dp[j][j + i - 1] = True
                            
        return dp[0][len(s) - 1]
        
        
