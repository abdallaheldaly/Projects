# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        result, current, level = [], [root], 1
        
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[ : : -1])
                
            level += 1
            current = next_level
            
        return result
    
    
