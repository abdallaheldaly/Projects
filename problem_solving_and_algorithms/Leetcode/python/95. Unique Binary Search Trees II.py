# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []
        else:
            return self.tree_constructor(1, n)

    def tree_constructor(self, m, n):
        results = []
        if m > n:
            results.append(None)
            return results

        for i in range(m, n + 1):
            l = self.tree_constructor(m, i - 1)
            r = self.tree_constructor(i + 1, n)
            
            for left_trees in l:
                for right_trees in r:
                    curr_node = TreeNode(i)
                    curr_node.left = left_trees
                    curr_node.right = right_trees
                    results.append(curr_node)

        return results
    
    
