import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
            
        exp = math.floor(math.log(n, 2))

        result = 0

        for i in range(exp, -1, -1):
            if n - (2 ** i) >= 0:
                n -= (2 ** i)
                result += 1

        return result