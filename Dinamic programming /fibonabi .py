# it the same 1 but with diff approcch time comblacety 
# befor logn^2 now log n
# 509. Fibonacci Number
class Solution:
    def rec(self, n, dp):
        # base case
        if n<=1:
            return n
        # recursive case
        if dp[n]!=-1:
            return dp[n]
        dp[n] = self.rec(n-1, dp) + self.rec(n-2, dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.rec(n, dp)