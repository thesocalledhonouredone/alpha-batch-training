class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        n = len(nums)

        dp = [0] * n
        m = 0
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        m = dp[-1]
        dp = [0] * n
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])

        for i in (3, n):
            dp[i-1] = max(dp[i-3] + nums[i], dp[i-2])
        
        return max(m, dp[-2])
    
"""
NEED TO SEE CORRECT SOLUTION

"""