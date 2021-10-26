# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        return self.pathSumRecu([], [], root, targetSum)

    def pathSumRecu(self, result, cur, root, targetSum):
        if root is None:
            return result
        
        if root.left is None and root.right is None and root.val == targetSum:
            result.append(cur + [root.val])
            return result
        
        cur.append(root.val)
        self.pathSumRecu(result, cur, root.left, targetSum - root.val)
        self.pathSumRecu(result, cur,root.right, targetSum - root.val)
        
        cur.pop()
        
        return result
    
    
