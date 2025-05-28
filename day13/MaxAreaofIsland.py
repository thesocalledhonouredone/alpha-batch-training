class Solution:

    def __init__(self):
        self.m = 0
        self.n = 0
        self.c = 0

    def dfs(self, g, i, j):
        if i < 0 or j < 0 or i >= self.n or j >= self.m or g[i][j] == 0:
            return

        g[i][j] = 0
        self.c += 1
        self.dfs(g, i-1, j) 
        self.dfs(g, i+1, j) 
        self.dfs(g, i, j-1) 
        self.dfs(g, i, j+1) 

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        marea = 0

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    self.c = 0
                    self.dfs(grid, i, j)
                    if self.c > marea:
                        marea = self.c
        
        return marea