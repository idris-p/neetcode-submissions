class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            digits = len(str(n))
            seen.add(n)
            total = 0
            for i in range(1, digits + 1):
                total += ((n % (10 ** i)) // (10 ** (i - 1))) ** 2
            n = total

        return n == 1