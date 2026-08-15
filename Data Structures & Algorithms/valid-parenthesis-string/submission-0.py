class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = maxLeft = 0

        for bracket in s:
            if bracket == "(":
                minLeft += 1
                maxLeft += 1
            elif bracket == ")":
                minLeft -= 1
                maxLeft -= 1
                if maxLeft < 0:
                    return False
            elif bracket == "*":
                minLeft = max(0, minLeft - 1)
                maxLeft += 1

        return minLeft <= 0 <= maxLeft