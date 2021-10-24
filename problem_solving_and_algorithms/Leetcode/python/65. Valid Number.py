class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip()
        try:
            s = float(s)
            return True
        except:
            return False


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s or '-' in s[1:] or '+' in s[1:]:
            return False
        if s[0] == '-' or s[0] == '+':
            if len(s) == 1:
                return False
            elif s[1] == 0:
                return False
        for c in s:
            if not ord('0') <= ord(c) <= ord('9') and c != '+' and c != '-':
                return False
        return True


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))