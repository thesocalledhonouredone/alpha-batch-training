class Solution:

    def __init__(self):
        self.res = list()

    def dfs(self, nums, i):
        if i == len(nums):
            self.res.append(list(nums))
            return
        
        j = i
        while j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
            j+=1    

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.dfs(nums, 0)
        return self.res