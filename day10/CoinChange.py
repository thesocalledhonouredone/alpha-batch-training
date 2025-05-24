class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        if amount == 0:
            return 0
        
        dp = [1000000] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for i in range(len(coins)):
                if coins[i] <= amt:
                    dp[amt] = min(dp[amt], 1+dp[amt-coins[i]])
        
        if dp[amount] == 1000000:
            return -1
        
        return dp[amount]
    
"""

time complexity: O(amount * len(coins))

"""

# MEMOIZED solution for the Coin Change Problem

class Another:
    def __init__(self):
        self.memo = None

    def cc(self, c, amt):
        if amt == 0:
            return 0
        
        if self.memo[amt] != -1:
            return self.memo[amt]
        
        mn = float('inf')

        for coin in c:
            if amt - coin >= 0:
                res = self.cc(c, amt - coin)
                
                if res != float('inf'):
                    mn = min(mn, 1 + res)
        
        self.memo[amt] = mn
        return self.memo[amt]

    def coinChange(self, coins, amount):
        self.memo = [-1] * (amount + 1)
        
        result = self.cc(coins, amount)
        
        return result if result != float('inf') else -1