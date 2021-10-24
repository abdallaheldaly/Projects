class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = ""
        for i in digits:
            num += str(i)
        num = int(num)
        num += 1
        num = str(num)
        ans = []
        
        for i in num:
            ans.append(int(i))
        return ans