class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        operators = {'+', '-', '*', '/'}
        
        if len(tokens) == 1: return int(tokens[0])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                sec_operand = stack.pop()
                fir_operand = stack.pop()
                tmp=0
                
                if token == '+':
                    tmp = fir_operand + sec_operand
                elif token == '-':
                    tmp = fir_operand - sec_operand
                elif token == '*':
                    tmp = fir_operand * sec_operand
                elif token == '/':
                    tmp = fir_operand / sec_operand
                    tmp = math.trunc(tmp)
                    
                stack.append(tmp)
                
        return stack.pop()
 
##################################

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        
        for token in tokens:
            if token not in operators:
                numerals.append(int(token))
            else:
                y, x = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](x * 1.0, y)))
                
        return numerals.pop()
