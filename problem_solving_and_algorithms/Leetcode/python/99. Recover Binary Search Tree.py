# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
      
        first_error = None
        second_error = None
        pre_node = TreeNode(float('-inf'))
        predecessor = None

        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if predecessor.right == None:
                    predecessor.right = root
                    root = root.left
                else:
                    if pre_node.val >= root.val and first_error == None:
                        first_error = pre_node
                    if pre_node.val >= root.val and first_error:
                        second_error = root
                    pre_node = root
                    
                    predecessor.right = None
                    root = root.right
            else:
                if pre_node.val >= root.val and first_error == None:
                    first_error = pre_node
                if pre_node.val >= root.val and first_error:
                    second_error = root
            
                pre_node = root

                root = root.right
        
        first_error.val, second_error.val = second_error.val, first_error.val
        
        
