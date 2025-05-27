class Solution:

    def __init__(self):
        self.result = list()

    def dfs(self, nums, a, i):
        self.result.append(list(a))
        j = i
        while j<len(nums):
            a.append(nums[j])
            self.dfs(nums, a, j+1)
            a.pop()
            j += 1

    def subsets(self, nums: list[int]) -> list[list[int]]:
        a = list()
        self.dfs(nums, a, 0)
        return self.result