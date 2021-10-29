# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def sumN(root, preSum):
            if not root:
                
                return 0
            
            preSum = preSum * 10 + root.val
            
            if not root.left and not root.right:
                return preSum
            return sumN(root.left, preSum) + sumN(root.right, preSum)
    
        return sumN(root, 0)
    
    
