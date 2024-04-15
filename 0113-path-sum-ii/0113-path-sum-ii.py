# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        s = 0
        res , temp = [] , []
        if not root: return res
        def dfs(node,s):
            s += node.val
            temp.append(node.val)
            if not node.left and not node.right:
                if s == target:
                    res.append(temp.copy())
                return
            if node.left:
                dfs(node.left,s)
                temp.pop()
            if node.right:
                dfs(node.right,s)
                temp.pop()
        dfs(root,s)
        return res
        