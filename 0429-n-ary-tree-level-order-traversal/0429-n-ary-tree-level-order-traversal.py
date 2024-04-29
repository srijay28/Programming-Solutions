"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        parent = [root]
        res = [[root.val]]
        temp = []
        children = []
        while True:
            children = []
            temp = []
            while parent:
                n = parent.pop(0)
                if n.children: children.extend(n.children)
            if len(children) == 0:
                break
            for i in children:
                temp.append(i.val)
            res.append(temp.copy())
            parent = children

        return res

            


        