class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix = [[ 0 for i in range(10) ] for j in range(10) ]
        

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        if matrix == None or len(matrix) == 0:
            pass
        elif len(matrix) == 1 and len(matrix[0]) == 1:
            pass
        else:
            rows_with_0 = [False] * len(matrix)
            cols_with_0 = [False] * len(matrix[0])
            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        rows_with_0[i] = True
                        cols_with_0[j] = True

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if rows_with_0[i] or cols_with_0[j]:
                        matrix[i][j] = 0