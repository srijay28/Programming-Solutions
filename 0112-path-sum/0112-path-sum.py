# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        s = 0
        flag = [False]
        if not root: return 0
        def dfs(node,s):
            s += node.val
            if not node.left and not node.right:
                if s == target:
                    flag[0] = True
                return
            if node.left:
                dfs(node.left,s)
            if node.right:
                dfs(node.right,s)
        dfs(root,s)
        return flag[0]
                

        