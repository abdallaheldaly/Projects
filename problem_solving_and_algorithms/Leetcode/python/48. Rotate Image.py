    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for i in xrange(n):
            for j in xrange(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
        
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
                
        return matrix
    
    
