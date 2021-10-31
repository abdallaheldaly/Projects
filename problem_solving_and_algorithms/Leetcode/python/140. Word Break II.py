class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        
        """
        
        
        self.memo = {}
        wordDict = set(wordDict)
        
        return self.solve(s, wordDict)
    def solve(self, s, wordDict):
        if not s:
            return ['']
        if s in self.memo:
            return self.memo[s]
        
        ret = []
        for i in range(1, len(s) + 1):
            if s[ : i] in wordDict:
                for j in self.solve(s[i : ],wordDict):
                    ret.append((s[ : i] + " " + j).strip())
                    
        self.memo[s] = ret
        return self.memo[s]
    
    
