class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        n = len(prices)
        dp = [0 for i in range(n)]
        ans = 0
        xmin = prices[0]
        
        for i in range(1, n):
            xmin = min(xmin, prices[i])
            dp[i] = max(dp[i], prices[i] - xmin)
            ans = max(ans, dp[i])
            
        xmax = [0 for i in range(n)]
        xmax[-1] =prices[-1]
        tempp = 0
        
        for i in range(n - 2, -1, -1):
            xmax[i] = max(xmax[i + 1], prices[i])
        xmin = [prices[-1], n]
        
        for i in range(n - 2, -1, -1):
            tempp = max(tempp,xmax[i + 1] - prices[i + 1])
            ans = max(ans, dp[i] + tempp)
            
        return ans
    
    
