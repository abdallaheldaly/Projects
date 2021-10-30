class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def ifPalindrom(a, b):
            if s[a : (b + 1)] == s[a : (b + 1)][ : : -1]: return True
            return False
        palindromDic = {}
        for i in range(len(s) -1, -1, -1):
            palindromDic[i] = []
            for j in range(i - 1, -1, -1):
                if ifPalindrom(j, i):
                    palindromDic[i].append(j)
        dp=[0 for i in range(len(s))]
        for i in range(1, len(s)):
            dp[i]=min(i,dp[i - 1] + 1)
            while len(palindromDic[i]) > 0:
                k = palindromDic[i].pop()
                if k == 0: 
                    dp[i] = 0;
                    break
                dp[i] = min(dp[i], dp[k - 1] + 1)
        return dp[len(s) - 1]
 
    def minCut2(self, s):
        isPalindrom = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPalindrom[j + 1][i - 1]):
                    isPalindrom[j][i] = True;
                    isPalindrom[i][j] = True
                    
        dp=[0 for i in range(len(s))]
        for i in range(1, len(s)):
            dp[i] = min(i, dp[i - 1] + 1)
            for j in range(i):
                if isPalindrom[j][i]:
                    if j == 0: 
                        dp[i] = 0;
                        break
                        
                    dp[i] = min(dp[i],dp[j - 1] + 1)
        return dp[len(s) - 1]
    
    
