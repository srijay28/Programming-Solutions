class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        l = len(grid)
        res = 0
        maxLocal = [[] for _ in range(l-2)]
        for i in range(0,l-2):
            for j in range(0,l-2):
                res = 0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        res = max(res,grid[x][y])
                maxLocal[i].append(res)
        return maxLocal

