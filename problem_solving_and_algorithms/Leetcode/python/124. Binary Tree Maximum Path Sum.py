# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
class Solution(object):
    maxVal = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathDown(root)
        return self.maxVal 

    def maxPathDown(self, cur):
        if not cur: 
            return 0
        left = max(0, self.maxPathDown(cur.left))
        right = max(0, self.maxPathDown(cur.right))
        self.maxVal = max(self.maxVal, left + right + cur.val)
        return max(left, right) + cur.val
    
    
