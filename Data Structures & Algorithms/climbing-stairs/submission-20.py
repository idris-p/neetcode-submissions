class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n, cache={}):
            if n == 1 or n == 2:
                return n
            if n in cache:
                return cache[n]

            result = dp(n-2, cache) + dp(n-1, cache)
            cache[n] = result
            return result

        return dp(n)