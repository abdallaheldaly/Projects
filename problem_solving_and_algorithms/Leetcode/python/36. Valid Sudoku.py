class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check(count):
            for char in count:
                if char != '.' and count[char] > 1:
                    return False
            return True
    
        for row in board:
            count_row = collections.Counter(row)
            if check(count_row) == False:
                return False
            
        n = len(board)
        
        for c in range(n):
            count_col = collections.Counter([board[r][c] for r in range(n)])
            if check(count_col) == False:
                return False
            
        for x in range(0, n, 3):
            for y in range(0, n, 3):
                sub = [board[x+dx][y+dy] for dx in range(3) for dy in range(3)]
                count_sub = collections.Counter(sub)
                if check(count_sub) == False:
                    return False
            
        return True  
    
