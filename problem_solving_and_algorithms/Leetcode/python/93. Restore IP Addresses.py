class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, path, res):
            
            if len(s) > (4 - len(path)) * 3:
                return
            
            if not s and len(path) == 4:
                res.append('.'.join(path))
                return
            
            for i in range(1, 4):
                if len(s) < i:
                    continue
                n = int(s[:i])
                if str(n) == s[ : i] and n <= 255:
                    dfs(s[i : ], path + [s[ : i]], res) 
                    
        if len(s) > 12: return []
        res = []
        dfs(s, [], res)
        
        return res
