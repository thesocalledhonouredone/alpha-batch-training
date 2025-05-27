class Solution:

    def __init__(self):
        self.res = list()

    def nqueen(self, n, r, col, tl , tr, b):
        
        if r == n:
            self.res.append(b)
            return
        
        for c in range(n):
            if col[c] == 0 and tl[r - c + n -1] == 0 and tr[r + c] == 0:
                b[r][c] = 'Q'
                col[c] = tl[r - c + n -1] = tr[r + c] = 1
                self.nqueen(n, r+1, col, tl, tr, c)
                col[c] = tl[r - c + n -1] = tr[r + c] = 0
                b[r][c] = '.'

    def solveNQueens(self, n: int) -> list[list[str]]:
        
        col = [0] * n
        tl = [0] * ((2*n)-1)
        tr = [0] * ((2*n)-1)

        s = '.' * n
        b = [s] * n

        self.nqueen(n, 0, col, tl, tr, b)
        return self.res