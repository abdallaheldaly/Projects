class Solution(object):
    def longestPalindrome(self, s):
        def assistant(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1

            return s[l + 1:r]
        
        newlist = ""

        for i in range(len(s)):
            dynamic_var = assistant(i, i)
            if len(dynamic_var) > len(newlist): newlist = dynamic_var
            dynamic_var = assistant(i, i + 1)
            if len(dynamic_var) > len(newlist): newlist = dynamic_var
        
        return newlist

            