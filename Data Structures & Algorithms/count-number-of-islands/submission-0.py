class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(row,col):

            queue = deque()
            queue.append((row,col))
            visited.add((row,col))
            while queue:
                r,c = queue.popleft()
                neighbours = [(0,1), (0,-1), (1,0), (-1,0)]

                for dr, dc in neighbours:
                    if ((r+dr)<0 or (c+dc)<0) or ((r+dr) == rows or (c+dc) == cols) or ((r+dr, c+dc) in visited) or grid[r+dr][c+dc]=="0":
                        continue
                    
                    queue.append((r+dr,c+dc))
                    visited.add((r+dr, c+dc))
                

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        
        return islands


            






