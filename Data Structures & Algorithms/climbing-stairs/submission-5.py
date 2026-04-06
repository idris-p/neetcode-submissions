class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {0: 0, 1: 1, 2: 2, 3: 3}

        def recursion(n):
            if n <= 3:
                return n

            if n - 2 in self.cache.keys():
                twoBelow = self.cache[n - 2]
            else:
                twoBelow = recursion(n - 2)
                self.cache[n - 2] = twoBelow

            if n - 1 in self.cache.keys():
                oneBelow = self.cache[n - 1]
            else:
                oneBelow = recursion(n - 1)
                self.cache[n - 1] = oneBelow

            return twoBelow + oneBelow

        return recursion(n)