class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1 for _ in range(n+1)]
        
        def fib(n):
            if n == 1 or n == 2:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = fib(n-1) + fib(n-2)
            return dp[n]
        return fib(n)