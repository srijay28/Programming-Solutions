class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start from pacific and atlantic respectively and do dfs and then intersect those sets
        rows , cols = len(heights) , len(heights[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        pacific , atlantic = set() , set()

        def dfs(r,c,visit,prevHeight):
            #write all rejection condition with "or"
            if ((r,c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols): 
            dfs(0,c,pacific,heights[0][c]) #for pacific ocean
            dfs(rows-1,c,atlantic,heights[rows-1][c]) #for pacific ocean
        
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])
        
        return list(pacific.intersection(atlantic))