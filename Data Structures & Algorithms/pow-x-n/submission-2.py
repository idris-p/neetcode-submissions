class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        negative = False
        if n < 0:
            negative = True
            n *= -1

        const = 1
        if n % 2 == 1:
            const = x

        power = self.myPow(x, n // 2)

        result =  power * power * const

        return result if not negative else 1 / result