# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        #Solved this mostly on my own 

        vertical_map = {} #keys are 
        q = [(root,0,0)] #root, hd, lvl
        res = []
        
        while q:
            node,hd,lvl = q.pop(0)
            if hd not in vertical_map:
                vertical_map[hd] = defaultdict(list)
            vertical_map[hd][lvl].append(node.val)
            if node.left : q.append((node.left,hd-1,lvl+1))
            if node.right: q.append((node.right,hd + 1,lvl+1))
        
        #Especially this part I solved on my own:

        cnt = 0
        for i in sorted(vertical_map): #this is hd values in sorted order
            res.append([])
            for j in sorted(vertical_map[i]): #this is lvl values in sorted order
                res[cnt].extend(sorted(vertical_map[i][j])) #so that all values of a single hd are in a row
            cnt += 1

        return res


        