# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        n = len(inorder)
        
        if n == 0:
            return None
        
        elif n == 1:
            return TreeNode(postorder[-1])
        
        else:
            root = TreeNode(postorder[-1])
            mid_inorder = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[ : mid_inorder], postorder[ : mid_inorder])
            root.right = self.buildTree(inorder[mid_inorder + 1 : ], postorder[mid_inorder : -1])
            
            return root
        
        
