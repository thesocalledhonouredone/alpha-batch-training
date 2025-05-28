class Solution:

    def dfs(self, g, i, j):
        if i < 0 or j < 0 or i >= len(g) or j >= len(g[0]) or g[i][j] == '0':
            return
        
        g[i][j] = '0'
        self.dfs(g, i-1, j)
        self.dfs(g, i, j-1)
        self.dfs(g, i+1, j)
        self.dfs(g, i, j+1)

    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        c = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    c += 1
                    self.dfs(grid, i, j)
        
        return c