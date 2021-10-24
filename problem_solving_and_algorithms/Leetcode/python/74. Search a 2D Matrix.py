class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix: return False
        row, col = len(matrix), len(matrix[0])
        if row == 0 or col == 0: 
            return False
        
        r, c = 0, col - 1
        for i in range(row):
            if target <= matrix[i][c]:
                l, r = 0, col - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] == target:
                        return True
                    if target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            else:
                continue
                
        return False