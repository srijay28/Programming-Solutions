# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        s = []
        if not root: return 0
        def dfs(node):
            s.append(str(node.val))

            if not node.left and not node.right:
                res.append(int(''.join(s)))
                return
            if node.left:
                dfs(node.left)
                s.pop()
            if node.right:
                dfs(node.right)
                s.pop()
        dfs(root)
        return sum(res)

        