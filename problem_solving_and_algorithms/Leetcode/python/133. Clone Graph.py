"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node: return node
        head = Node(node.val, [])
        map = {node: head}
        
        queue = collections.deque()
        queue.append(node)
        
        while queue:
            tmp = queue.popleft()
            for n in tmp.neighbors:
                if n in map.keys():
                    map[tmp].neighbors.append(map[n])
                else:
                    map[n] = Node(n.val, [])
                    map[tmp].neighbors.append(map[n])
                    queue.append(n)
        return head
    
    
