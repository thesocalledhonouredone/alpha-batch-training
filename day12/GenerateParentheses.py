class Solution:

    def __init__(self):
        self.res = list()

    def dfs(self, n, l, r, s):
        if len(s) == 2 * n:
            self.res.append(s)
        if l < n:
            self.dfs(n, l+1, r, str(s + '('))
        if r < l:
            self.dfs(n, l, r+1, str(s + ')'))
        
    def generateParenthesis(self, n: int) -> list[str]:
        self.dfs(n , 0, 0, "")
        return self.res