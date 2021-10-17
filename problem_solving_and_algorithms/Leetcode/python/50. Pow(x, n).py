class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        power = abs(n)
        res = 1.0
        
        while power:
            if power & 1:
                res *= x
            x *= x
            power >>= 1
        if n < 0:
            return 1 / res
        
        return res
