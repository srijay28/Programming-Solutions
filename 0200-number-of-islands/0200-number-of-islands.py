class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # this is a breadth first search algorithm
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        islands = 0

        #implementation of bfs : will run only once after being called
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            #top , down , right , left
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            while q:
                r,c = q.popleft()
                
                for dr,dc in directions:
                    nr , nc = r + dr, c + dc
                    #check the validity of these cordinates
                    #check if they are equal to 1
                    #check if they are visited
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc)) 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    #do bfs from this point
                    bfs(r,c)
                    islands += 1
        return islands

        


    