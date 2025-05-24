class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fun(n, memo):
            if n <= 2:
                memo[n] = n
                return memo[n]
            if memo[n] != 1:
                return memo[n]
            memo[n] = fun(n-1) + fun(n-2)
            return memo[n]

        memo = [-1] * (n+1)

        return fun(n, memo)