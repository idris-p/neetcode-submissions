class Solution:
    def climbStairs(self, n: int) -> int:
        function = {1: 1, 2: 2} # n: f(n)

        def f(n):
            if n in function:
                return function[n]
            function[n] = f(n-2) + f(n-1)
            return function[n]
        return f(n)