class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        s = sum(nums)

        if s % 2 != 0:
            return False
        
        dp = [0] * (s//2 + 1)
        dp[0] = 1

        for x in nums:
            i = s//2
            while i >= 0:
                if dp[i] == 1 and i+x <= s//2:
                    dp[i+x] = 1
                i -= 1
        
        return bool(dp[s//2])