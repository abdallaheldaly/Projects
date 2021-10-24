class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """     
        return map(lambda x: int(x, 2), self.grayBit(n))
 
    def grayBit(self, n):
        if n == 0:
            return ['0']
        if n == 1:
            return ['0', '1']
        prev = self.grayBit(n - 1)
        return ['0' + s for s in prev] + ['1' + s for s in prev[ : : -1]]
