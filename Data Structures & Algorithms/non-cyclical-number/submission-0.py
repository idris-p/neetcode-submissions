class Solution:
    def isHappy(self, n: int) -> bool:
        number = str(n)
        total = 0
        seen = set()

        while total != 1:
            total = 0
            for digit in number:
                total += int(digit) ** 2
            number = str(total)
           
            if total in seen:
                return False

            seen.add(total)

        return True