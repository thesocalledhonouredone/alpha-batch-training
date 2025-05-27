class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)

        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        
        x = total + target // 2
        dp = [0] * (x+1)
        dp[0] = 1

        for i in range(len(nums)):
            j = x
            while j >= nums[i]:
                dp[j] += dp[j-nums[i]]
                j -= 1
        
        return dp[-1]

