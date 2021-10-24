class Solution(object):
    def generateParenthesis(self, n):

        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result
    
    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)

########################################################

class Solution(object):
    def generateParenthesis(self, n):

        if n == 0: 
            return []
        ls = ['(']
        end = False
        
        while not end:
            end = True
            temp = []
            
            for i in range(len(ls)):
                l = ls[i].count('(')
                r = ls[i].count(')')
                
                if l == n:
                    if l > r:
                        ls[i] += (')' * (l - r))
                    else:
                        end = False
                        if l > r:
                            temp.append(ls[i] + ')')
                            ls[i] += '('
                            
            ls += temp
        return ls