class Solution:
    def __init__(self):
        self.res = list()

    def dfs(self, a, target, i, t):
        if target == 0:
            self.res.append(list(t))
            return
        if target < 0:
            return

        j = i
        while j < len(a):
            t.append(a[j])
            self.dfs(a, target - a[j], j, t)
            t.pop()
            j += 1

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        t = []
        self.dfs(candidates, target, 0, t)
        return self.res